# Smart Attendance System Using Face Detection and OpenCV

## Project Overview

The Smart Attendance System is an automated attendance management system that uses Face Recognition and OpenCV to identify students and mark attendance. The system captures live video through a webcam, detects faces, compares them with previously stored face encodings, and automatically records attendance with date and time. It also saves the attendance image and provides a voice notification after successful recognition.

---

## Features

- Face Detection using OpenCV
- Face Recognition using face_recognition library
- Automatic Attendance Marking
- Date and Time Recording
- Attendance stored in CSV file
- Attendance Image Saving
- Voice Notification
- Duplicate Attendance Prevention
- Real-Time Face Recognition
- Confidence Percentage Display

---

## Technologies Used

- Python 3.10
- OpenCV
- face_recognition
- NumPy
- Pickle
- CSV
- pyttsx3
- OS Module
- Datetime Module

---

## Project Structure

```
Smart_Attendance_System/
│
├── dataset/
│   ├── Dhiksha.jpg
│   ├── Student2.jpg
│
├── attendance_images/
│
├── encodings.pickle
├── encode_face.py
├── attendance.py
├── attendance.csv
├── requirements.txt
└── README.md
```

---

## Installation

Install Python packages:

```bash
pip install opencv-python
pip install face_recognition
pip install numpy
pip install pyttsx3
```

Or install all packages:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1

Place student face images inside the **dataset** folder.

Example:

```
dataset/
Dhiksha.jpg
Karthika.jpg
```

---

### Step 2

Generate Face Encodings

```bash
python encode_face.py
```

This creates:

```
encodings.pickle
```

---

### Step 3

Run Attendance System

```bash
python attendance.py
```

---

## Working Process

1. Load stored face encodings.
2. Open webcam.
3. Detect face.
4. Generate face encoding.
5. Compare with stored encodings.
6. Identify student.
7. Calculate confidence.
8. Mark attendance.
9. Save attendance in CSV.
10. Save attendance image.
11. Give voice announcement.
12. Prevent duplicate attendance.

---

## Attendance Output

Example:

| Name | Date | Time | Status |
|------|------------|----------|---------|
| Dhiksha | 2026-07-31 | 10:25:30 | Present |

---

## Attendance Image

Captured images are automatically saved inside

```
attendance_images/
```

Example

```
Dhiksha_2026-07-31_10-25-30.jpg
```

---

## Voice Notification

After successful recognition, the system announces:

```
Attendance marked for Dhiksha
```

---

## Advantages

- Paperless attendance
- Saves time
- Accurate face recognition
- Easy to use
- Prevents proxy attendance
- Automatic record maintenance
- Low cost
- Real-time processing

---

## Limitations

- Requires proper lighting
- Camera quality affects accuracy
- Face should be clearly visible
- Works only with registered faces

---

## Future Enhancements

- Cloud Database Integration
- Mobile Application
- SMS Notification
- Email Attendance Report
- Face Mask Recognition
- Anti-Spoofing Detection
- Multi-Camera Support
- Database Integration using MySQL
- QR Code Attendance Backup
- AI-based Face Recognition Improvement

---

## Developed By

**Dhiksha**

Department of Computer Science with Cyber Security

PSGR Krishnammal College for Women

---

## Conclusion

The Smart Attendance System provides a secure, accurate, and automated solution for attendance management using Face Detection and Face Recognition. It minimizes manual work, improves accuracy, prevents duplicate attendance, and stores attendance records efficiently.