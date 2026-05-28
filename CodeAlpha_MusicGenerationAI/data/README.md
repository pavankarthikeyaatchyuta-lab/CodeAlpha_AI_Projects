# 📁 Music Generation Training Dataset

This directory contains the training MIDI files used by the LSTM Recurrent Neural Network to learn note sequences and chord structures.

---

## 🎼 MIDI Datasets

We have programmatically populated this folder with diverse, structured MIDI files to ensure the LSTM model learns realistic and varied musical patterns instead of basic scale repetitions:

1.  **`chords_progression.mid`**
    *   **Description:** Implements common triad chord progressions (e.g., C Major, G Major, A Minor, F Major) in multiple keys.
    *   **Purpose:** Teaches the network harmony, chord stack configurations, and root transitions.
2.  **`melody_pattern.mid`**
    *   **Description:** A sequence of melodic motifs containing step-wise movements, rhythmic offsets, and minor/major interval leaps.
    *   **Purpose:** Helps the network predict natural melodic contours and rhythmic variations.
3.  **`minor_scale_arpeggios.mid`**
    *   **Description:** Multi-octave rising and falling arpeggiated patterns across A Minor, C Major, and F Major structures.
    *   **Purpose:** Guides the network to generate smooth, flowing runs and faster sequences of notes.
4.  **`dummy_scale.mid`**
    *   **Description:** A standard single-octave ascending and descending C-major scale.
    *   **Purpose:** Acts as a basic fallback pattern.

---

## ⚙️ Programmatic Generator

The training MIDI files are generated programmatically using the script `generate_rich_midi.py`. You can adjust pitch intervals, chord types, or note durations inside the script and re-run it:

```bash
python generate_rich_midi.py
```

This will automatically overwrite the `.mid` files in this folder with your updated arrangements.
