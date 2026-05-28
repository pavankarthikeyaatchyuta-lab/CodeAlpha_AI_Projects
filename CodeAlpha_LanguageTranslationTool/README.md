# 🌍 AI Language Translator

A real-time, multi-modal language translation application featuring a futuristic, glassmorphic dark-theme UI. The application supports text input, live speech-to-text recording, quick translations, instant audio playback (text-to-speech), and a session history panel.

---

## 🚀 Key Features

*   **Multi-Modal Inputs:** Enter text manually or use the built-in microphone for real-time speech recognition.
*   **Instant Audio Playback:** Listen to translated text spoken in native accents using text-to-speech synthesis.
*   **Dynamic UI Update:** Voice recognition outputs are instantly written directly into the text editor for editability.
*   **Historical Log:** Automatically keeps a cached log of your last 5 translations in a glassmorphic history card.
*   **Unified Shared UI:** Custom backgrounds, Outfits typography, interactive neon hover states, and smooth slide-up entrance animations.

---

## 🛠️ Technical Stack & Architecture

*   **Frontend Framework:** Built using **Streamlit**.
*   **Translation Engine:** Powered by `deep-translator` wrapping Google Translate APIs for zero-config, highly accurate translations.
*   **Speech-to-Text (STT):** Leverages Python's `SpeechRecognition` library coupled with Google's speech recognition APIs.
*   **Text-to-Speech (TTS):** Powered by `gTTS` (Google Text-to-Speech) for vocalization of output.
*   **Design System:** Styled programmatically using custom CSS injected from the shared `Shared_UI/ui_utils.py` template.

---

## 📦 Prerequisites & Installation

Ensure you have Python 3.10 to 3.13 installed.

```bash
# Install the project requirements
pip install -r requirements.txt
```

> [!NOTE]
> If the `pyaudio` library fails to compile due to missing C++ compilers on Windows, you can install it using pre-compiled wheels via:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🏃 Run the Application

Start the Streamlit application from the project root or the project folder:

```bash
python -m streamlit run app.py
```
By default, the application serves locally on `http://localhost:8501`.
