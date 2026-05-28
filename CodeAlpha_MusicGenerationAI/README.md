# 🎵 AI Music Composer (LSTM)

A deep learning music generation platform that trains a recurrent neural network (LSTM) on MIDI sequences and synthesizes new, custom MIDI arrangements directly into warm, retro 8-bit synthetic audio tracks.

---

## 🚀 Key Features

*   **LSTM Recurrent Network:** Built with Keras/TensorFlow, featuring multiple LSTM layers, dropout regularization, and softmax categorical notes/chords prediction.
*   **Rich Training Dataset:** Programmatically populated with diverse MIDI patterns (chord progressions, scales, rising/falling arpeggios) in `data/` for complex melodic generation.
*   **WAV Audio Synthesis:** Uses `numpy` and `scipy.io.wavfile` to compile MIDI tracks into WAV files on the fly, bypassing heavyweight system dependencies like FluidSynth/Musescore.
*   **Warm Timbre Additive Synthesis:** Combines fundamental note frequencies with 2nd, 3rd, and 4th harmonics alongside an exponential ADSR decay envelope for a warm, vintage electric-piano feel.
*   **Active Cache Tracking:** Linked to code changes and modification timestamps, invalidating and reloading resource caches dynamically.
*   **Pulsing Ring Background:** Custom dark-themed layout with pulsing rings that scale dynamically to represent soundwaves.

---

## 🛠️ Technical Stack & Architecture

*   **Frontend Framework:** Built using **Streamlit**.
*   **Deep Learning Backend:** Powered by `TensorFlow / Keras` for sequential model building, training, and next-step prediction.
*   **MIDI Parser:** Uses `music21` to parse note pitch and duration details, extract chords, and compile predicted elements into standard MIDI files.
*   **Audio DSP Synthesis:** Custom-coded DSP engine utilizing `numpy` for additive harmonic wave generation, and `scipy` for writing 16-bit PCM WAV containers.

---

## 📁 Programmatic Dataset

The repository includes a helper script `data/generate_rich_midi.py` which populates the training dataset programmatically:
*   `chords_progression.mid`: Common chord progressions (I-V-vi-IV).
*   `melody_pattern.mid`: Diverse scale leaps and melodic motifs.
*   `minor_scale_arpeggios.mid`: Multi-octave rising and falling minor arpeggios.

Run the generator script to re-generate or modify patterns:
```bash
python data/generate_rich_midi.py
```

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
By default, the application serves locally on `http://localhost:8503`.
