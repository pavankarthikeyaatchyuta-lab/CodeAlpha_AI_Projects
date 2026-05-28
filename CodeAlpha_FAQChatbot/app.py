import streamlit as st
import sys
import os
import json
import time
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import speech_recognition as sr

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

# Force reload ui_utils to prevent Streamlit/Python caching issues
if "ui_utils" in sys.modules:
    del sys.modules["ui_utils"]

try:
    from ui_utils import apply_custom_css, render_header
except ImportError:
    st.error("Failed to load UI utilities.")
    st.stop()

# Configure Page
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS
apply_custom_css("chatbot")

# Download NLTK data (runs once)
@st.cache_resource
def download_nltk_data():
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)
    except:
        pass

download_nltk_data()

# Load FAQ Data and setup NLP models
@st.cache_resource
def load_faq_system(file_mtime):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'faq_data.json')
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return None, None, None

    questions = [item['question'] for item in data]
    answers = [item['answer'] for item in data]

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(questions)

    return vectorizer, tfidf_matrix, answers

faq_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'faq_data.json')
faq_mtime = os.path.getmtime(faq_file_path) if os.path.exists(faq_file_path) else 0
vectorizer, tfidf_matrix, answers = load_faq_system(faq_mtime)

if not vectorizer:
    st.error("FAQ data missing! Please ensure faq_data.json exists.")
    st.stop()

def get_best_answer(user_question, threshold=0.3):
    user_vec = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vec, tfidf_matrix)
    best_idx = similarities.argmax()
    
    if similarities[0, best_idx] >= threshold:
        return answers[best_idx]
    else:
        return "I'm sorry, I don't have an answer for that in my FAQ database. Could you try rephrasing your question?"

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am an AI FAQ Assistant. How can I help you today?"}
    ]

# Sidebar
with st.sidebar:
    st.markdown("<h2 class='glow-text'>System Panel</h2>", unsafe_allow_html=True)
    st.markdown("This chatbot uses **TF-IDF Vectorization** and **Cosine Similarity** to match your question against a predefined dataset.")
    
    st.markdown("---")
    st.markdown("### Voice Search")
    if st.button("🎤 Ask with Voice", use_container_width=True):
        with st.spinner("Accessing microphone..."):
            voice_prompt = recognize_speech()
            if voice_prompt:
                st.session_state.messages.append({"role": "user", "content": voice_prompt})
                # Get response
                answer = get_best_answer(voice_prompt)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                st.rerun()
                
    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am an AI FAQ Assistant. How can I help you today?"}
        ]
        st.rerun()

# Main UI
render_header("AI Chat Assistant", "Natural Language Processing FAQ Chatbot")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a question about AI..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Get the actual answer
        answer = get_best_answer(prompt)
        
        # Simulate stream of response with typing effect
        for chunk in answer.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
