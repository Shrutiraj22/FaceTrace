from deepface import DeepFace
import cv2
import os

def recognize_faces(frame):
    cv2.imwrite("temp.jpg", frame)
    authorized_dir = "authorized_faces"
    for img in os.listdir(authorized_dir):
        try:
            result = DeepFace.verify("temp.jpg", os.path.join(authorized_dir, img), enforce_detection=False)
            if result["verified"]:
                return True
        except Exception:
            continue
    return False
