import numpy as np
import sounddevice as sd
from scipy.signal import butter, sosfilt

# ============================================================
# SETTINGS
# ============================================================

SAMPLE_RATE = 48000

# Smaller block = lower latency but more CPU overhead
BLOCK_SIZE = 256

# ANC is most useful at lower frequencies
LOWPASS_HZ = 800

# Anti-noise strength
# Start LOW. Increase carefully.
GAIN = 10

# Approximate system/acoustic delay.
# Experiment with this.
DELAY_MS = 1.0

INPUT_DEVICE = None
OUTPUT_DEVICE = None

# ============================================================
# LOW-PASS FILTER
# ============================================================

sos = butter(
    6,
    LOWPASS_HZ,
    btype="lowpass",
    fs=SAMPLE_RATE,
    output="sos"
)

filter_state = np.zeros((sos.shape[0], 2))

# Delay buffer
delay_samples = int(SAMPLE_RATE * DELAY_MS / 1000)

delay_buffer = np.zeros(delay_samples, dtype=np.float32)


# ============================================================
# AUDIO CALLBACK
# ============================================================

def callback(indata, outdata, frames, time, status):

    global filter_state
    global delay_buffer

    if status:
        print(status)

    # --------------------------------------------------------
    # Get microphone signal
    # --------------------------------------------------------

    microphone = indata[:, 0].astype(np.float32)

    # --------------------------------------------------------
    # Remove DC offset
    # --------------------------------------------------------

    microphone -= np.mean(microphone)

    # --------------------------------------------------------
    # Low-pass filter
    # --------------------------------------------------------

    filtered, filter_state = sosfilt(
        sos,
        microphone,
        zi=filter_state
    )

    # --------------------------------------------------------
    # Create delayed signal
    # --------------------------------------------------------

    combined = np.concatenate(
        (delay_buffer, filtered)
    )

    delayed = combined[:frames]

    delay_buffer = combined[frames:]

    # --------------------------------------------------------
    # Generate anti-noise
    #
    # Negative sign = phase inversion
    # --------------------------------------------------------

    anti_noise = -GAIN * delayed

    # --------------------------------------------------------
    # Prevent clipping
    # --------------------------------------------------------

    anti_noise = np.clip(
        anti_noise,
        -0.8,
        0.8
    )

    # --------------------------------------------------------
    # Output
    # --------------------------------------------------------

    outdata[:, 0] = anti_noise

    # If stereo headphones
    if outdata.shape[1] > 1:
        outdata[:, 1] = anti_noise


# ============================================================
# START AUDIO STREAM
# ============================================================

print("======================================")
print(" Python Experimental ANC")
print("======================================")
print()
print("Sample rate :", SAMPLE_RATE)
print("Block size  :", BLOCK_SIZE)
print("Low-pass    :", LOWPASS_HZ, "Hz")
print("Gain        :", GAIN)
print("Delay       :", DELAY_MS, "ms")
print()
print("Press Ctrl+C to stop.")
print()

try:

    with sd.Stream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        dtype="float32",
        channels=(1, 2),
        device=(INPUT_DEVICE, OUTPUT_DEVICE),
        callback=callback
    ):
        while True:
            sd.sleep(1000)

except KeyboardInterrupt:

    print("\nANC stopped.")

except Exception as e:

    print("\nERROR:")
    print(e)