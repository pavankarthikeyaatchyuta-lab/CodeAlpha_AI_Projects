import streamlit as st
import sys
import os
import time

# Force reload ui_utils to prevent Streamlit/Python caching issues
if "ui_utils" in sys.modules:
    del sys.modules["ui_utils"]
if "model_utils" in sys.modules:
    del sys.modules["model_utils"]

try:
    from ui_utils import apply_custom_css, render_header
except ImportError:
    st.error("Failed to load UI utilities.")
    st.stop()

from model_utils import MusicModel

# Configure Page
st.set_page_config(
    page_title="AI Music Composer",
    page_icon="🎵",
    layout="wide"
)

# Apply CSS
apply_custom_css("music")

# Initialize Model
@st.cache_resource
def get_model(mtime):
    return MusicModel(data_dir=os.path.join(os.path.dirname(__file__), "data"))

model_utils_path = os.path.join(os.path.dirname(__file__), "model_utils.py")
mtime = os.path.getmtime(model_utils_path) if os.path.exists(model_utils_path) else 0
music_model = get_model(mtime)

# UI Layout
render_header("AI Music Composer", "LSTM-based AI Music Generation System")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 class='glow-text'>Model Training</h3>", unsafe_allow_html=True)
    st.info("The system uses an LSTM network to learn sequences from MIDI files. If the data folder is empty, a dummy C-major scale will be created automatically for demonstration.")
    
    if st.button("🚀 Train Model (Fast Demo Mode)", use_container_width=True):
        with st.spinner("Training LSTM Model... This might take a minute."):
            try:
                # Train with small epochs for demo
                result = music_model.train(epochs=5, batch_size=8)
                st.success(result)
                st.balloons()
            except Exception as e:
                st.error(f"Training failed: {e}")

with col2:
    st.markdown("<h3 class='glow-text'>Music Generation</h3>", unsafe_allow_html=True)
    st.markdown("Once the model is trained, click below to generate a new MIDI sequence.")
    
    length = st.slider("Sequence Length", min_value=10, max_value=100, value=30, step=10)
    
    if st.button("🎹 Generate Music", use_container_width=True):
        model_path = os.path.join(os.path.dirname(__file__), "model.keras")
        if not os.path.exists(model_path):
            st.error("Model not found! Please train the model first.")
        else:
            with st.spinner("Generating AI Music and Synthesizing Audio..."):
                try:
                    if not music_model.model:
                        music_model.load_existing_model()
                    
                    output_path = os.path.join(os.path.dirname(__file__), "generated_output.mid")
                    music_model.generate_music(num_notes=length, output_file=output_path)
                    
                    # Synthesize to WAV for browser audio playback
                    wav_path = os.path.join(os.path.dirname(__file__), "generated_output.wav")
                    music_model.synthesize_to_wav(output_path, wav_path)
                    
                    st.success("Music generated successfully!")
                    
                    # Audio Player
                    st.markdown("#### 🎧 Play Generated Music (Retro 8-Bit Synth)")
                    with open(wav_path, "rb") as wav_file:
                        st.audio(wav_file.read(), format="audio/wav")
                    
                    with open(output_path, "rb") as file:
                        btn = st.download_button(
                            label="📥 Download Generated MIDI",
                            data=file,
                            file_name="ai_music.mid",
                            mime="audio/midi",
                            use_container_width=True
                        )
                except Exception as e:
                    st.error(f"Generation Error: {e}")
