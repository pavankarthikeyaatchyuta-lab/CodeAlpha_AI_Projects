# CodeAlpha AI Internship - Production-Level AI Projects

This repository contains a suite of four fully functional, production-ready Artificial Intelligence projects developed for the CodeAlpha AI Internship. All applications are built using **Python** and **Streamlit**, featuring a shared, premium, futuristic dark glassmorphic user interface.

---

## 🌌 Shared Premium UI System
Every project in this suite is styled using a custom design system located in [Shared_UI/ui_utils.py](./Shared_UI/ui_utils.py). Key characteristics of the styling include:
*   **Futuristic Dark Mode:** A rich linear gradient background (`#0b0f19` to `#1a1b41`) tailored for AI dashboards.
*   **Glassmorphism & Liquid Glass:** Semi-transparent container cards with custom blur backdrops, subtle border gradients, and interactive hover transformations.
*   **Glow Effects:** Interactive text shadowing and neon button accents (`#00d2ff` & `#92FE9D`).
*   **Micro-Animations:** Fade-in entrances and floating key elements to make the interface feel responsive and alive.

---

## 📁 Projects Directory Structure

```text
CodeAlpha_AI_Projects/
├── Shared_UI/                             # Shared UI Styling & CSS Utilities
│   └── ui_utils.py
├── CodeAlpha_LanguageTranslationTool/     # Project 1: AI Language Translator
│   ├── app.py
│   └── requirements.txt
├── CodeAlpha_FAQChatbot/                  # Project 2: NLP FAQ Chatbot
│   ├── app.py
│   ├── faq_data.json
│   └── requirements.txt
├── CodeAlpha_MusicGenerationAI/           # Project 3: AI Music Composer
│   ├── app.py
│   ├── model_utils.py
│   └── requirements.txt
├── CodeAlpha_ObjectDetectionTracking/     # Project 4: AI Vision Tracker
│   ├── app.py
│   ├── webcam_app.py
│   └── requirements.txt
└── README.md                              # Main Workspace Documentation
```

---

## 🛠️ Project Portfolio

### 🌍 Project 1: AI Language Translator
A real-time translation app that supports multi-modal user input and output.
*   **Core Logic:** Powered by the `deep-translator` API wrapper (Google Translate) for text conversion.
*   **Voice Inputs:** Utilizes `SpeechRecognition` to capture live audio from the microphone and convert it to editable text.
*   **Voice Outputs:** Utilizes Google Text-to-Speech (`gTTS`) to read the translation aloud.
*   **Features:** Real-time speech-to-text, text-to-speech feedback, responsive output card, and translation history cache.
*   **Folder:** [CodeAlpha_LanguageTranslationTool](./CodeAlpha_LanguageTranslationTool/)

### 🤖 Project 2: NLP FAQ Chatbot
A semantic, vector-based chatbot that handles common AI questions.
*   **Core Logic:** Tokenizes and preprocesses inputs using `NLTK`, then applies `TF-IDF Vectorization` (via `scikit-learn`) to translate queries and database questions into semantic vectors.
*   **Matching System:** Utilizes `cosine_similarity` to retrieve the mathematically closest answer from a pre-configured FAQ JSON file (`faq_data.json`).
*   **Features:** Natural stream-typing animations, clean message layouts, conversational memory, sidebar utility controls, and customizable similarity threshold matching.
*   **Folder:** [CodeAlpha_FAQChatbot](./CodeAlpha_FAQChatbot/)

### 🎵 Project 3: AI Music Composer (LSTM)
An deep learning music generator that trains an LSTM neural network on MIDI note sequences.
*   **Core Logic:** Uses `music21` to parse and write MIDI formats. Builds a recurrent Neural Network (`LSTM`) in `TensorFlow/Keras` to predict subsequent notes from sequences.
*   **Features:** FAST demo training option directly from the UI, custom sequence length generation, real-time training progress logs, and automatic MIDI file generation and downloader.
*   **Folder:** [CodeAlpha_MusicGenerationAI](./CodeAlpha_MusicGenerationAI/)

### 👁️ Project 4: AI Vision Object Detection & Tracking
A real-time computer vision platform tracking unique instances of physical objects in video streams.
*   **Core Logic:** Leverages `YOLOv8` (via `ultralytics` API) for state-of-the-art object detection.
*   **Features:** Bounding box styling, object labels, confidence score overlays, and frame-by-frame tracker persistency. Supports video file upload and real-time canvas rendering.
*   **Folder:** [CodeAlpha_ObjectDetectionTracking](./CodeAlpha_ObjectDetectionTracking/)

---

## 🚀 Quick Start & Installation

Ensure you have **Python 3.10 to 3.13** installed.

### 1. General Setup
We recommend using a virtual environment to manage dependencies:
```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate
```

### 2. Running a Specific Project
Navigate to the directory of the project you want to run, install the unpinned requirements (optimized for compatibility with new Python environments like Python 3.13), and start Streamlit:

#### Project 1: Language Translation Tool
```bash
cd CodeAlpha_LanguageTranslationTool
pip install -r requirements.txt
python -m streamlit run app.py
```

#### Project 2: FAQ Chatbot
```bash
cd CodeAlpha_FAQChatbot
pip install -r requirements.txt
python -m streamlit run app.py
```

#### Project 3: Music Generation AI
```bash
cd CodeAlpha_MusicGenerationAI
pip install -r requirements.txt
python -m streamlit run app.py
```

#### Project 4: Object Detection & Tracking
```bash
cd CodeAlpha_ObjectDetectionTracking
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 💡 Troubleshooting & Windows Compatibility
*   **PyAudio Installation Failures (Project 1):** If the `pyaudio` library fails to compile, it is usually because C compilers are missing. Run:
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```
*   **NumPy Version Conflicts:** Version numbers in the `requirements.txt` configurations have been unpinned to allow `pip` to automatically resolve compiled packages (like `numpy`) that have official support for Python 3.13.
