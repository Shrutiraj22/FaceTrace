import cv2
import time
from motion_detector import detect_motion
from face_recognizer import recognize_faces
from alert import trigger_alert, log_event

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    start_time = time.time()

    while cap.isOpened():
        motion_detected, frame_with_boxes = detect_motion(frame1, frame2)

        if motion_detected:
            faces_recognized = recognize_faces(frame1)
            log_event("Motion Detected")

            if not faces_recognized:
                trigger_alert()
                log_event("Unknown face detected")

    
        if time.time() - start_time > 10:
            print("Auto-stopping after 10 seconds.")
            break

        
        cv2.putText(frame_with_boxes, "Press 'Q' or ESC to Quit", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Surveillance Feed", frame_with_boxes)

        key = cv2.waitKey(10) & 0xFF
        if key == ord('q') or key == 27:
            print("Stopped by user.")
            break

      
        frame1 = frame2
        ret, frame2 = cap.read()

    cap.release()
    cv2.destroyAllWindows()
