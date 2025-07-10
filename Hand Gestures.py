import cv2
import mediapipe as mp
import pyautogui


def volumecontrol(thumb_and_pointer, pointer_and_middle, thumb_and_middle):
    if thumb_and_pointer > 25 and pointer_and_middle < 30 and thumb_and_middle > 15:
        pyautogui.press("volumeup")

    if thumb_and_pointer > 30 and pointer_and_middle < 25 and thumb_and_middle > 15:
        pyautogui.press("volumeup", presses=2)

    if thumb_and_pointer > 35 and pointer_and_middle < 20 and thumb_and_middle > 15:
        pyautogui.press("volumeup", presses=5)

    if thumb_and_pointer < 15 and pointer_and_middle > 10:
        pyautogui.press("volumedown")

    if thumb_and_pointer < 10 < pointer_and_middle:
        pyautogui.press("volumedown", presses=2)

    if thumb_and_pointer < 5 and pointer_and_middle > 10:
        pyautogui.press("volumedown", presses=5)


def cursorcontrol(delta_x, delta_y, thumb_and_pointer, pointer_and_middle, thumb_and_middle):
    if delta_x > 25 and thumb_and_middle < 10 < pointer_and_middle:
        cv2.putText(image, "", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        pyautogui.moveRel(-30, 0)

    if delta_x < -25 and thumb_and_middle < 10 < pointer_and_middle:
        cv2.putText(image, "", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        pyautogui.moveRel(30, 0)

    if delta_y > 10 and thumb_and_middle < 10 < pointer_and_middle:
        cv2.putText(image, "", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        pyautogui.moveRel(0, 30)

    if delta_y < -10 and thumb_and_middle < 10 < pointer_and_middle:
        cv2.putText(image, "", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        pyautogui.moveRel(0, -30)


def click(thumb_and_pointer, pointer_and_middle, thumb_and_middle, thumb_and_ringman, thumb_and_pinky):
    if thumb_and_pointer < 10 and pointer_and_middle < 10 and thumb_and_ringman < 10 and thumb_and_pinky < 10:
        pyautogui.rightClick()
        cv2.waitKey(100)
    elif thumb_and_pointer < 10 and pointer_and_middle < 10:
        pyautogui.click()
        cv2.waitKey(100)


webcam = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
drawutils = mp.solutions.drawing_utils
x1 = x2 = y1 = y2 = x3 = y3 = x4 = y4 = x5 = y5 = 0
previous_x1, previous_y1 = 0, 0

while True:

    _, image = webcam.read()
    frame_height, frame_width, depth = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = hands.process(rgb_image)

    capthand = output.multi_hand_landmarks

    if capthand:

        for hand2 in capthand:

            drawutils.draw_landmarks(image, hand2)
            landmarks = hand2.landmark

            for id, landmarks in enumerate(landmarks):
                x = int(landmarks.x * frame_width)
                y = int(landmarks.y * frame_height)

                if id == 8:  # Finger: Pointer
                    cv2.circle(img=image, center=(x, y), radius=5, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y

                if id == 4:  # Figner: Thumb
                    cv2.circle(img=image, center=(x, y), radius=5, color=(0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y

                if id == 12:  # Finger: Middle
                    cv2.circle(img=image, center=(x, y), radius=5, color=(255, 0, 0), thickness=3)
                    x3 = x
                    y3 = y

                if id == 16:  # Finger: Ringman
                    cv2.circle(img=image, center=(x, y), radius=5, color=(0, 255, 0), thickness=3)
                    x4 = x
                    y4 = y

                if id == 20:  # Finger: Pinky
                    cv2.circle(img=image, center=(x, y), radius=5, color=(255, 255, 0), thickness=3)
                    x5 = x
                    y5 = y

        delta_x = x1 - previous_x1
        delta_y = y1 - previous_y1

        # Update previous positions
        previous_x1 = x1
        previous_y1 = y1

        thumb_and_pointer = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
        thumb_and_pointer = thumb_and_pointer ** 0.5
        thumb_and_pointer = thumb_and_pointer // 4

        pointer_and_middle = ((x1 - x3) ** 2 + (y1 - y3) ** 2)
        pointer_and_middle = pointer_and_middle ** 0.5
        pointer_and_middle = pointer_and_middle // 4

        thumb_and_middle = ((x2 - x3) ** 2 + (y2 - y3) ** 2)
        thumb_and_middle = thumb_and_middle ** 0.5
        thumb_and_middle = thumb_and_middle // 4

        thumb_and_ringman = ((x2 - x4) ** 2 + (y2 - y4) ** 2)
        thumb_and_ringman = thumb_and_ringman ** 0.5
        thumb_and_ringman = thumb_and_ringman // 4

        thumb_and_pinky = ((x2 - x5) ** 2 + (y2 - y5) ** 2)
        thumb_and_pinky = thumb_and_pinky ** 0.5
        thumb_and_pinky = thumb_and_pinky // 4

        cursorcontrol(delta_x, delta_y, thumb_and_pointer, pointer_and_middle, thumb_and_middle)
        volumecontrol(thumb_and_pointer, pointer_and_middle, thumb_and_middle)
        click(thumb_and_pointer, pointer_and_middle, thumb_and_middle, thumb_and_ringman, thumb_and_pinky)

    cv2.imshow("Python Based Mini Vision Pro", image)
    key = cv2.waitKey(10)
    if key == 27:
        webcam.release()
        cv2.destroyAllWindows()
        break
