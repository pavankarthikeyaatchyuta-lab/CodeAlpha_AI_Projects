# 🤖 AI Chat Assistant (FAQ Chatbot)

A semantic, vector-based conversational assistant that answers frequently asked questions about artificial intelligence and technology. Features a glassmorphic interface with natural stream-typing animations, clear message layouts, and sidebar utility controls.

---

## 🚀 Key Features

*   **Semantic Matching:** Pre-processes questions and query inputs, converting them into high-dimensional TF-IDF vectors for matching.
*   **Vector Cosine Similarity:** Calculates similarity mathematically, returning the most relevant answer above a configurable threshold.
*   **Natural Typing Simulation:** Simulates live chat responsiveness by outputting answer text in a natural typing stream.
*   **Voice Search Support:** Speak commands/questions directly into your microphone to submit a query.
*   **Active Cache Invalidation:** Auto-detects manual updates to the FAQ database (`faq_data.json`) and invalidates cache resources on the fly.
*   **Drifting Orb Background:** A custom dark-theme layout with slow-drifting neon blue and violet gradient orbs in 3D perspective space.

---

## 🛠️ Technical Stack & Architecture

*   **Frontend Framework:** Built using **Streamlit**.
*   **Natural Language Processing (NLP):** Powered by `NLTK` (Natural Language Toolkit) for tokenization and preprocessing.
*   **Vectorization & Retrieval:** Uses `scikit-learn`'s `TfidfVectorizer` to build question vectors, and `cosine_similarity` for nearest-neighbor match retrieval.
*   **Voice Recognition:** Powered by `SpeechRecognition` translating user audio via Google's Web Speech API.

---

## 📁 Database Configuration

The chatbot questions and answers are managed inside `faq_data.json`:
```json
[
    {
        "question": "What is AI?",
        "answer": "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines..."
    }
]
```
Add new question-answer blocks to the list to expand the chatbot's knowledge base. The changes will be re-vectorized automatically.

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
By default, the application serves locally on `http://localhost:8502`.
