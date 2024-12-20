import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load known face images and their encodings
itachi_img = face_recognition.load_image_file('itachi.jpg')
kakashi_img = face_recognition.load_image_file('kakashi.jpg')

itachi_face_encoding = face_recognition.face_encodings(itachi_img)[0]
kakashi_face_encoding = face_recognition.face_encodings(kakashi_img)[0]

# Add more faces if needed
known_face_encodings = [itachi_face_encoding, kakashi_face_encoding]
known_face_names = ["Itachi", "Kakashi"]

# List to track students
students = known_face_names.copy()

# Get current date for the attendance file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Open CSV file for writing attendance
with open(f"{current_date}.csv", "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Name", "Time"])

    # Initialize variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture frame from camera. Exiting...")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Process every frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Check for matches
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                face_names.append(name)

                # Mark attendance
                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H:%M:%S")
                    csv_writer.writerow([name, current_time])

        # Display results on the frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame was resized
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.75, (255, 255, 255), 1)

        # Display the frame
        cv2.imshow("Attendance System", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
