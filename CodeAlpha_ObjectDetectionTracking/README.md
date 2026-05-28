# 👁️ AI Vision Object Detection & Tracking

A real-time computer vision dashboard designed to run object detection and persistent tracking on video uploads and local webcam feeds. 

---

## 🚀 Key Features

*   **YOLOv8 Detection & Tracking:** Leverages the state-of-the-art YOLOv8 nano model for high-efficiency, real-time object classification and bounding box rendering.
*   **Persistent Tracking (YOLOv8 ByteTrack):** Employs YOLOv8's built-in `track(persist=True)` tracking algorithm to assign persistent IDs to unique instances of detected objects across video frames.
*   **Dual Feed Support:** Process uploaded video files (mp4, avi, mov) frame-by-frame or run live capture via your local webcam.
*   **Interactive HUD Panel:** 
    *   **Live Rate Indicator:** Displays real-time frames-per-second (FPS) processing rates in a custom HUD gauge.
    *   **Targets Tracked:** Dynamic breakdown of currently tracked objects categorized by class name with live counts.
*   **Laser Sweep Animation:** A themed laser scanner grid backdrop indicating computer vision execution.

---

## 🛠️ Technical Stack & Architecture

*   **Frontend Framework:** Built using **Streamlit**.
*   **Computer Vision Framework:** Powered by `ultralytics` YOLOv8.
*   **Image Processing:** Utilizes `OpenCV` (`cv2`) for video capture, frame extraction, color space conversion, and webcam operations.
*   **Headless Optimization:** Structured with `opencv-python-headless` requirements to prevent GUI/display conflicts on cloud hosts and Docker containers.

---

## 📦 Prerequisites & Installation

Ensure you have Python 3.10 to 3.13 installed.

```bash
# Install the project requirements
pip install -r requirements.txt
```

---

## 🏃 Run the Application

Start the Streamlit application from the project root or the project folder:

```bash
python -m streamlit run app.py
```
By default, the application serves locally on `http://localhost:8504`.

For a local webcam feed in a standalone OpenCV window, you can run the CLI script directly:
```bash
python webcam_app.py
```
Press `q` to close the webcam window.
