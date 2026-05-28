import streamlit as st
import cv2
import tempfile
import sys
import os
import time
from ultralytics import YOLO

# Add parent directory to path to import shared UI
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Force reload Shared_UI.ui_utils to prevent Streamlit/Python caching issues
if "Shared_UI.ui_utils" in sys.modules:
    del sys.modules["Shared_UI.ui_utils"]
if "Shared_UI" in sys.modules:
    del sys.modules["Shared_UI"]

try:
    from Shared_UI.ui_utils import apply_custom_css, render_header, render_glass_card
except ImportError:
    st.error("Failed to load Shared UI. Please run from the project root.")
    st.stop()

# Configure Page
st.set_page_config(
    page_title="AI Vision Tracker",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS
apply_custom_css("vision")

@st.cache_resource
def load_model():
    return YOLO('yolov8n.pt')

model = load_model()

render_header("AI Vision Tracking", "Real-time YOLOv8 Object Detection and Tracking Dashboard")

# Sidebar settings
with st.sidebar:
    st.markdown("<h2 class='glow-text'>Configuration</h2>", unsafe_allow_html=True)
    source_type = st.radio("Select Input Source", ["📹 Video File", "🎥 Live Webcam"])
    confidence = st.slider("Confidence Threshold", min_value=0.1, max_value=1.0, value=0.25, step=0.05)

# Main layout
col_video, col_stats = st.columns([3, 1])

with col_video:
    st.markdown("<h3 class='glow-text'>Vision Feed</h3>", unsafe_allow_html=True)
    stframe = st.empty()

with col_stats:
    st.markdown("<h3 class='glow-text'>Analysis HUD</h3>", unsafe_allow_html=True)
    fps_placeholder = st.empty()
    stats_placeholder = st.empty()

# Processing Logic
cap = None
is_running = False

if source_type == "📹 Video File":
    uploaded_file = st.file_uploader("Upload Video File", type=['mp4', 'avi', 'mov'])
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        cap = cv2.VideoCapture(tfile.name)
        is_running = True
else:
    # Live Webcam
    if st.button("🚀 Start Webcam", use_container_width=True):
        cap = cv2.VideoCapture(0)
        is_running = True

if is_running and cap is not None:
    stop_button = st.button("⏹️ Stop Stream", use_container_width=True)
    prev_time = time.time()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or stop_button:
            break
            
        # Run YOLOv8 tracking
        results = model.track(frame, persist=True, conf=confidence)
        
        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        
        # Extract object counts
        counts = {}
        boxes = results[0].boxes
        if boxes is not None and len(boxes) > 0:
            class_ids = boxes.cls.cpu().numpy().astype(int)
            names = model.names
            for cid in class_ids:
                cname = names[cid]
                counts[cname] = counts.get(cname, 0) + 1
        
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        
        # Render Video Frame
        stframe.image(annotated_frame, channels="RGB", use_container_width=True)
        
        # Update FPS HUD
        fps_placeholder.markdown(f"""
            <div class="glass-container" style="padding: 1rem; margin-bottom: 1rem; text-align: center;">
                <span style="font-size: 0.9rem; color: #94a3b8;">SYSTEM RATE</span><br/>
                <span class="glow-text" style="font-size: 2.2rem; font-weight: 800;">{fps:.1f} FPS</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Update Detection Stats HUD
        stats_html = "<div class='glass-container' style='padding: 1.5rem;'>"
        stats_html += "<h4 class='glow-text' style='margin-top:0;'>Targets Tracked</h4>"
        if counts:
            for item, count in counts.items():
                stats_html += f"""
                <div style='display:flex; justify-content:space-between; margin-bottom:0.5rem; font-size:1rem;'>
                    <span style='color:#e2e8f0; font-weight:500;'>🤖 {item.capitalize()}</span>
                    <span style='color:var(--accent-color); font-weight:700;'>{count}</span>
                </div>
                """
        else:
            stats_html += "<span style='color:#64748b;'>No targets detected.</span>"
        stats_html += "</div>"
        stats_placeholder.markdown(stats_html, unsafe_allow_html=True)
        
    cap.release()
    st.success("Vision processing complete.")
