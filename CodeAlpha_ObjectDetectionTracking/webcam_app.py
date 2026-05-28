import cv2
from ultralytics import YOLO
import time

def run_tracker():
    print("Initializing AI Vision Tracker...")
    
    # Load YOLOv8 model
    model = YOLO('yolov8n.pt')
    
    # Open local webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Tracker started. Press 'q' to quit.")

    prev_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        # Run YOLOv8 tracking
        results = model.track(frame, persist=True)

        # Visualize the results
        annotated_frame = results[0].plot()

        # Display FPS
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display output
        cv2.imshow("AI Vision Tracker (Webcam)", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_tracker()
