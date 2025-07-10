# import cv2
# import face_recognition
# import pandas as pd
# from datetime import datetime
# import os
#
# # Directory containing known face images
# known_faces_dir = 'F:\\New folder\\Attendence with face/know_faces'
#
# # Load known faces
# known_faces = []
# known_names = []
# for filename in os.listdir(known_faces_dir):
#     if filename.endswith('.jpg') or filename.endswith('.png'):
#         image = face_recognition.load_image_file(f"{known_faces_dir}/{filename}")
#         encoding = face_recognition.face_encodings(image)[0]
#         known_faces.append(encoding)
#         known_names.append(filename.split('.')[0])
#
#
# # Function to capture image
# def capture_image():
#     cam = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             print("Failed to grab frame")
#             break
#         cv2.imshow('Press Space to capture', frame)
#         if cv2.waitKey(1) & 0xFF == ord(' '):
#             break
#     cam.release()
#     cv2.destroyAllWindows()
#     return frame if ret else None
#
#
# # Function to recognize face
# def recognize_face(captured_image):
#     face_encodings = face_recognition.face_encodings(captured_image)
#     if len(face_encodings) == 0:
#         print("No faces detected in the image.")
#         return None
#     captured_encoding = face_encodings[0]
#     matches = face_recognition.compare_faces(known_faces, captured_encoding)
#     if True in matches:
#         first_match_index = matches.index(True)
#         return known_names[first_match_index]
#     return None
#
#
# # Function to mark attendance
# def mark_attendance(student_name, file='attendance.xlsx'):
#     now = datetime.now()
#     current_date = now.strftime("%Y-%m-%d")
#     current_time = now.strftime("%H:%M:%S")
#     try:
#         df = pd.read_excel(file)
#     except FileNotFoundError:
#         df = pd.DataFrame(columns=["Name", "Date", "Time"])
#     new_record_df = pd.DataFrame({"Name": [student_name], "Date": [current_date], "Time": [current_time]})
#     df = pd.concat([df, new_record_df], ignore_index=True)
#     df.to_excel(file, index=False)
#
#
# # Main execution
# def main():
#     image = capture_image()
#     if image is None:
#         return
#     student_name = recognize_face(image)
#     if student_name is None:
#         print("Student not recognized!")
#         return
#     mark_attendance(student_name)
#     print(f"Attendance marked for {student_name}")
#
#
# if __name__ == "__main__":
#     main()
