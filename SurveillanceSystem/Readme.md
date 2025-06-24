# Surveillance System Using Computer Vision

A Python-based surveillance system that detects motion, performs face recognition using DeepFace, and raises alerts for unauthorized access using real-time webcam footage.


## Features

*  Real-time video capture from webcam
*  Motion detection using frame differencing
*  Face recognition using DeepFace
*  Audio alert for unrecognized faces
*  Logging of motion and alert events
*  Auto-terminate system after a set time (default: 10 seconds)
*  Exit manually using 'Q' or 'ESC' keys

---

## Tech Stack

* Python 3.9+
* OpenCV (`opencv-python`)
* DeepFace (TensorFlow-based)
* Pillow (for alternate image handling)

---

## Project Structure

```
SurveillanceSystem/
├── main.py                 # Orchestrates detection, recognition, alert
├── motion_detector.py      # Motion detection logic
├── face_recognizer.py      # DeepFace-based recognition
├── alert.py                # Alerting and logging utility
├── log.csv                 # Log of detected events
└── authorized_faces/       # Folder containing known face images
└── streamlit_app.py        # streamlit dashboard
```


## How to Run

### 1. Clone the repo & install dependencies:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install opencv-python deepface
```

> On Mac: If using TensorFlow 2.18+, run `pip install tf-keras`

### 2. Add face images

Put one or more front-facing face images of authorized people in the `authorized_faces/` folder.

### 3. Run the system:

```bash
python main.py
```

* Press **Q** or **ESC** to quit manually.
* System stops automatically after 10 seconds (can be changed).



## Future Improvements

* Streamlit/Tkinter GUI
* Cloud or email alert integration
* Integration with CCTV or external camera
* Add GUI face authorization system




## Created by

**Shruti Raj** — B.Tech CSE (Big Data Analytics) | 📍India
