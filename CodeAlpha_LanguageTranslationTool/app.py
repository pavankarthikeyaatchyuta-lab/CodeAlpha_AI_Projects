import streamlit as st
import sys
import os
import json
import base64
from datetime import datetime
from deep_translator import GoogleTranslator
from gtts import gTTS
import speech_recognition as sr
import io

# Force reload ui_utils to prevent Streamlit/Python caching issues
if "ui_utils" in sys.modules:
    del sys.modules["ui_utils"]

try:
    from ui_utils import apply_custom_css, render_header, render_glass_card
except ImportError:
    st.error("Failed to load UI utilities.")
    st.stop()

# Configure Page
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply CSS
apply_custom_css("translator")

# Available Languages
LANGUAGES = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
    'Italian': 'it', 'Portuguese': 'pt', 'Russian': 'ru', 'Japanese': 'ja',
    'Korean': 'ko', 'Chinese (Simplified)': 'zh-CN', 'Hindi': 'hi', 'Arabic': 'ar'
}

# Initialize Session State
if 'history' not in st.session_state:
    st.session_state.history = []
if 'src_text' not in st.session_state:
    st.session_state.src_text = ""

def text_to_speech(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp
    except Exception as e:
        st.error(f"TTS Error: {e}")
        return None

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        audio = r.listen(source, timeout=5)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.warning("Could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Speech Recognition error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")
    return ""

# UI Layout
render_header("AI Translation Engine", "Real-time AI-powered text and voice translation with glassmorphic UI.")

# Main Interface
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 class='glow-text'>Input</h3>", unsafe_allow_html=True)
    source_lang_name = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0, key='src_lang')
    
    # Text Input
    source_text = st.text_area("Enter text to translate...", value=st.session_state.src_text, height=200, key='src_text')
    
    # Voice Input Button
    if st.button("🎤 Start Voice Input", use_container_width=True):
        with st.spinner("Accessing microphone..."):
            voice_text = recognize_speech()
            if voice_text:
                st.session_state.src_text = voice_text
                st.rerun()

with col2:
    st.markdown("<h3 class='glow-text'>Output</h3>", unsafe_allow_html=True)
    target_lang_name = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1, key='tgt_lang')
    
    translated_text = ""
    audio_fp = None
    
    if st.button("✨ Translate Now", use_container_width=True) and source_text:
        with st.spinner("Translating..."):
            try:
                src_code = LANGUAGES[source_lang_name]
                tgt_code = LANGUAGES[target_lang_name]
                
                # Perform Translation
                translator = GoogleTranslator(source='auto', target=tgt_code)
                translated_text = translator.translate(source_text)
                
                # Generate Audio
                audio_fp = text_to_speech(translated_text, tgt_code)
                
                # Save to History
                st.session_state.history.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "source_lang": source_lang_name,
                    "target_lang": target_lang_name,
                    "original": source_text,
                    "translated": translated_text
                })
            except Exception as e:
                st.error(f"Translation Error: {e}")

    # Display Result
    st.text_area("Translation Result", value=translated_text, height=200, key='tgt_text', disabled=True)
    
    # Audio Player
    if audio_fp:
        st.markdown("#### 🎧 Listen")
        st.audio(audio_fp, format='audio/mp3')

st.markdown("---")

# History Section
st.markdown("<h3 class='glow-text'>Translation History</h3>", unsafe_allow_html=True)
if st.session_state.history:
    for item in reversed(st.session_state.history[-5:]): # Show last 5
        content = f"""
        **{item['source_lang']} &rarr; {item['target_lang']}** <span style='float:right; color:#64748b; font-size:0.8rem;'>{item['timestamp']}</span>
        <br/><br/>
        **Original:** {item['original']} <br/>
        **Translated:** {item['translated']}
        """
        render_glass_card("", content)
else:
    st.info("No translation history yet.")
