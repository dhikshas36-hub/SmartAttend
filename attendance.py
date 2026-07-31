import cv2
import face_recognition
import pickle
import numpy as np
import csv
import os
from datetime import datetime
import pyttsx3


# =========================================
# LOAD FACE ENCODINGS
# =========================================

with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

knownEncodings = data["encodings"]
knownNames = data["names"]

if len(knownEncodings) == 0:
    print("No face encodings found!")
    print("Please run encode_face.py first.")
    exit()


# =========================================
# ATTENDANCE CSV FILE
# =========================================

attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):

    with open(attendance_file, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Name",
            "Date",
            "Time",
            "Status"
        ])


# =========================================
# ATTENDANCE IMAGE FOLDER
# =========================================

image_folder = "attendance_images"

if not os.path.exists(image_folder):

    os.makedirs(image_folder)


# =========================================
# VOICE ENGINE
# =========================================

engine = pyttsx3.init()

engine.setProperty("rate", 150)


# =========================================
# PREVENT DUPLICATE ATTENDANCE
# =========================================

marked_names = set()


# =========================================
# OPEN CAMERA
# =========================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("Unable to open camera!")

    exit()


print("Smart Attendance System Started")
print("Press Q to Exit")


# =========================================
# MAIN LOOP
# =========================================

while True:

    ret, frame = cap.read()

    if not ret:

        print("Camera Error!")

        break


    # Convert BGR to RGB

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # Detect faces

    face_locations = face_recognition.face_locations(
        rgb
    )


    # Encode faces

    face_encodings = face_recognition.face_encodings(
        rgb,
        face_locations
    )


    # =========================================
    # PROCESS EACH FACE
    # =========================================

    for face_encoding, face_location in zip(
        face_encodings,
        face_locations
    ):

        top, right, bottom, left = face_location


        # Calculate face distance

        face_distances = face_recognition.face_distance(
            knownEncodings,
            face_encoding
        )


        if len(face_distances) == 0:

            continue


        # Find best match

        best_match_index = np.argmin(
            face_distances
        )


        best_distance = face_distances[
            best_match_index
        ]


        # Default name

        name = "Unknown"


        # =========================================
        # STRICT FACE MATCHING
        # =========================================

        if best_distance < 0.42:

            name = knownNames[
                best_match_index
            ]


            # =========================================
            # CONFIDENCE PERCENTAGE
            # =========================================

            confidence = (
                1 - best_distance
            ) * 100


            # Keep percentage between 0 and 100

            confidence = max(
                0,
                min(
                    100,
                    confidence
                )
            )


            # =========================================
            # MARK ATTENDANCE ONLY ONCE
            # =========================================

            if name not in marked_names:

                marked_names.add(name)


                # Current date and time

                now = datetime.now()


                date = now.strftime(
                    "%Y-%m-%d"
                )


                time = now.strftime(
                    "%H:%M:%S"
                )


                # =========================================
                # SAVE ATTENDANCE IN CSV
                # =========================================

                with open(
                    attendance_file,
                    "a",
                    newline=""
                ) as f:

                    writer = csv.writer(f)


                    writer.writerow([
                        name,
                        date,
                        time,
                        "Present"
                    ])


                # =========================================
                # SAVE FACE IMAGE
                # =========================================

                image_name = (
                    name
                    + "_"
                    + date
                    + "_"
                    + time.replace(
                        ":",
                        "-"
                    )
                    + ".jpg"
                )


                image_path = os.path.join(
                    image_folder,
                    image_name
                )


                cv2.imwrite(
                    image_path,
                    frame
                )


                # =========================================
                # TERMINAL OUTPUT
                # =========================================

                print(
                    f"{name} - Present"
                )


                print(
                    f"Date: {date}"
                )


                print(
                    f"Time: {time}"
                )


                print(
                    f"Confidence: {confidence:.2f}%"
                )


                print(
                    f"Image Saved: {image_path}"
                )


                # =========================================
                # VOICE ANNOUNCEMENT
                # =========================================

                message = (
                    "Attendance marked for "
                    + name
                )


                engine.say(
                    message
                )


                engine.runAndWait()


        else:

            confidence = (
                1 - best_distance
            ) * 100


            confidence = max(
                0,
                min(
                    100,
                    confidence
                )
            )


        # =========================================
        # BOX COLOR
        # =========================================

        if name == "Unknown":

            color = (
                0,
                0,
                255
            )

        else:

            color = (
                0,
                255,
                0
            )


        # =========================================
        # FACE RECTANGLE
        # =========================================

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            color,
            2
        )


        # =========================================
        # DISPLAY NAME AND CONFIDENCE
        # =========================================

        display_text = (
            f"{name} - "
            f"{confidence:.2f}%"
        )


        cv2.putText(
            frame,
            display_text,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )


    # =========================================
    # DISPLAY CAMERA WINDOW
    # =========================================

    cv2.imshow(
        "Smart Attendance System",
        frame
    )


    # =========================================
    # PRESS Q TO EXIT
    # =========================================

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# =========================================
# CLOSE CAMERA
# =========================================

cap.release()

cv2.destroyAllWindows()


print(
    "Smart Attendance System Closed"
)