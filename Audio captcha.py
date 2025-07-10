from captcha.audio import AudioCaptcha
import random

def generate_captcha(length=6):
    characters = "1234567890"
    captcha_Text = ''.join(random.choices(characters, k=length))
    return captcha_Text


audio = AudioCaptcha()
captcha_text = generate_captcha()
print(f"CAPTCHA Texts: {captcha_text}")
audio_captcha = audio.generate(captcha_text)
audio.write(captcha_text, 'Audio_Captcha.wav')
print("Audio CAPTCHA Generated: Audio_Captcha.wav")