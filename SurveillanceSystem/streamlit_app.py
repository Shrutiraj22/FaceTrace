import streamlit as st
import cv2
import numpy as np
import tempfile
from motion_detector import detect_motion
from face_recognizer import recognize_faces
from alert import trigger_alert, log_event
import time

st.set_page_config(page_title="Surveillance Dashboard", layout="wide")
st.title("🛡️ AI Surveillance System Dashboard")

run = st.checkbox('Start Surveillance')

frame_window = st.image([])
log_box = st.empty()

if run:
    cap = cv2.VideoCapture(0)
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    start_time = time.time()

    while run and cap.isOpened():
        motion_detected, frame_with_boxes = detect_motion(frame1, frame2)

   
        if motion_detected:
            recognized = recognize_faces(frame1)
            log_event("Motion Detected")

            if not recognized:
                trigger_alert()
                log_event("Unknown Face Detected")

        frame_rgb = cv2.cvtColor(frame_with_boxes, cv2.COLOR_BGR2RGB)
        frame_window.image(frame_rgb)

        with open("log.csv", "r") as f:
            logs = f.read()
        log_box.text_area("📝 Event Log", logs, height=200)

    
        frame1 = frame2
        ret, frame2 = cap.read()

        if time.time() - start_time > 10:
            st.warning("⏱️ Auto-stopped after 10s")
            break

    cap.release()
