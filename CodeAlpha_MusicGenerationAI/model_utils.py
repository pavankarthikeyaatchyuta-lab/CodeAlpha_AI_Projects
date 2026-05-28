import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Activation
from music21 import converter, instrument, note, chord, stream
import glob
import os
import random

class MusicModel:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.sequence_length = 10 # Short for fast demo
        self.model = None
        self.int_to_note = {}
        self.note_to_int = {}
        self.n_vocab = 0
        self.network_input = []

    def ensure_dummy_data(self):
        """Creates a simple C-major scale MIDI if the data folder is empty."""
        os.makedirs(self.data_dir, exist_ok=True)
        if not glob.glob(f"{self.data_dir}/*.mid"):
            output_notes = []
            scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
            # Make a simple repetitive pattern so the LSTM has something to learn
            for _ in range(4): 
                for p in scale:
                    new_note = note.Note(p)
                    new_note.quarterLength = 0.5
                    output_notes.append(new_note)
            
            midi_stream = stream.Stream(output_notes)
            midi_stream.write('midi', fp=os.path.join(self.data_dir, "dummy_scale.mid"))

    def get_notes(self):
        self.ensure_dummy_data()
        notes = []
        for file in glob.glob(f"{self.data_dir}/*.mid"):
            try:
                midi = converter.parse(file)
                notes_to_parse = None
                try: 
                    s2 = instrument.partitionByInstrument(midi)
                    notes_to_parse = s2.parts[0].recurse() 
                except: 
                    notes_to_parse = midi.flatten().notes
                for element in notes_to_parse:
                    if isinstance(element, note.Note):
                        notes.append(str(element.pitch))
                    elif isinstance(element, chord.Chord):
                        notes.append('.'.join(str(n) for n in element.normalOrder))
            except Exception as e:
                print(f"Failed to parse {file}: {e}")
        return notes

    def prepare_sequences(self, notes):
        pitches = sorted(set(item for item in notes))
        self.n_vocab = len(pitches)
        self.note_to_int = dict((n, num) for num, n in enumerate(pitches))
        self.int_to_note = dict((num, n) for num, n in enumerate(pitches))
        
        network_input = []
        network_output = []
        for i in range(0, len(notes) - self.sequence_length, 1):
            sequence_in = notes[i:i + self.sequence_length]
            sequence_out = notes[i + self.sequence_length]
            network_input.append([self.note_to_int[char] for char in sequence_in])
            network_output.append(self.note_to_int[sequence_out])
        
        n_patterns = len(network_input)
        if n_patterns == 0:
            raise ValueError("Not enough notes to create sequences.")
            
        self.network_input = network_input
        network_input_reshaped = np.reshape(network_input, (n_patterns, self.sequence_length, 1))
        network_input_reshaped = network_input_reshaped / float(self.n_vocab)
        network_output = tf.keras.utils.to_categorical(network_output, num_classes=self.n_vocab)
        return network_input_reshaped, network_output

    def build_model(self, network_input_reshaped):
        model = Sequential()
        model.add(LSTM(64, input_shape=(network_input_reshaped.shape[1], network_input_reshaped.shape[2]), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(64))
        model.add(Dense(32))
        model.add(Dropout(0.2))
        model.add(Dense(self.n_vocab))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        self.model = model

    def train(self, epochs=5, batch_size=16):
        import tempfile
        import shutil
        import time
        notes = self.get_notes()
        X, y = self.prepare_sequences(notes)
        self.build_model(X)
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=1)
        
        model_path = os.path.join(os.path.dirname(self.data_dir), "model.keras")
        
        # Save to local system temp directory first to avoid OneDrive real-time sync locks
        temp_dir = tempfile.gettempdir()
        temp_model_path = os.path.join(temp_dir, f"temp_music_model_{int(time.time())}.keras")
        
        try:
            self.model.save(temp_model_path)
            
            # Copy to final destination with retry logic for active sync locks
            for i in range(5):
                try:
                    shutil.copy2(temp_model_path, model_path)
                    break
                except Exception as e:
                    if i == 4:
                        raise e
                    time.sleep(0.5)
        finally:
            # Clean up temp file
            if os.path.exists(temp_model_path):
                try:
                    os.remove(temp_model_path)
                except:
                    pass
                    
        return "Model trained successfully."

    def load_existing_model(self):
        model_path = os.path.join(os.path.dirname(self.data_dir), "model.keras")
        if os.path.exists(model_path):
            self.model = load_model(model_path)
            notes = self.get_notes()
            self.prepare_sequences(notes)
            return True
        return False

    def generate_music(self, num_notes=50, output_file="generated.mid"):
        if not self.model or not self.network_input:
            raise Exception("Model is not trained.")
            
        start = np.random.randint(0, len(self.network_input)-1)
        pattern = self.network_input[start]
        prediction_output = []

        for note_index in range(num_notes):
            prediction_input = np.reshape(pattern, (1, len(pattern), 1))
            prediction_input = prediction_input / float(self.n_vocab)
            prediction = self.model.predict(prediction_input, verbose=0)
            index = np.argmax(prediction)
            result = self.int_to_note[index]
            prediction_output.append(result)
            pattern.append(index)
            pattern = pattern[1:len(pattern)]

        offset = 0
        output_notes = []
        for pattern in prediction_output:
            if ('.' in pattern) or pattern.isdigit():
                notes_in_chord = pattern.split('.')
                notes = []
                for current_note in notes_in_chord:
                    new_note = note.Note(int(current_note))
                    new_note.storedInstrument = instrument.Piano()
                    notes.append(new_note)
                new_chord = chord.Chord(notes)
                new_chord.offset = offset
                output_notes.append(new_chord)
            else:
                new_note = note.Note(pattern)
                new_note.offset = offset
                new_note.storedInstrument = instrument.Piano()
                output_notes.append(new_note)
            offset += 0.5

        midi_stream = stream.Stream(output_notes)
        midi_stream.write('midi', fp=output_file)
        return output_file

    def synthesize_to_wav(self, midi_file, wav_file):
        """Synthesizes a MIDI file into a retro 8-bit WAV file using sine wave generation in numpy/scipy."""
        from scipy.io import wavfile
        
        # Parse MIDI
        midi_stream = converter.parse(midi_file)
        notes = midi_stream.flatten().notes
        
        sample_rate = 22050
        tempo = 120
        seconds_per_beat = 60.0 / tempo
        
        # Determine total duration
        max_time = 0
        for element in notes:
            max_time = max(max_time, element.offset + element.duration.quarterLength)
            
        total_seconds = max_time * seconds_per_beat + 1.0
        total_samples = int(total_seconds * sample_rate)
        audio_data = np.zeros(total_samples, dtype=np.float32)
        
        for element in notes:
            start_time = element.offset * seconds_per_beat
            duration = element.duration.quarterLength * seconds_per_beat
            start_sample = int(start_time * sample_rate)
            end_sample = int((start_time + duration) * sample_rate)
            
            if end_sample > total_samples:
                end_sample = total_samples
                
            t = np.linspace(0, duration, end_sample - start_sample, endpoint=False)
            
            # Frequencies
            freqs = []
            if isinstance(element, note.Note):
                freqs.append(element.pitch.frequency)
            elif isinstance(element, chord.Chord):
                for n in element.notes:
                    freqs.append(n.pitch.frequency)
                    
            # Synthesize warmer sound using fundamental + harmonics and a decay envelope
            note_wave = np.zeros(end_sample - start_sample, dtype=np.float32)
            for freq in freqs:
                # Add fundamental frequency + harmonics
                wave = np.sin(2 * np.pi * freq * t)
                wave += 0.4 * np.sin(2 * np.pi * (2 * freq) * t)
                wave += 0.2 * np.sin(2 * np.pi * (3 * freq) * t)
                wave += 0.1 * np.sin(2 * np.pi * (4 * freq) * t)
                
                # ADSR-like Envelope (Attack & Decay)
                attack_time = 0.02 # 20ms attack
                attack_samples = int(attack_time * sample_rate)
                
                envelope = np.ones_like(t)
                if len(t) > 0:
                    if attack_samples > len(t):
                        attack_samples = len(t)
                    if attack_samples > 0:
                        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
                        
                    decay_samples = len(t) - attack_samples
                    if decay_samples > 0:
                        decay_t = np.linspace(0, 4, decay_samples)
                        envelope[attack_samples:] = np.exp(-decay_t)
                        
                wave *= envelope
                note_wave += wave
                
            if len(freqs) > 0:
                note_wave /= len(freqs)
                
            audio_data[start_sample:end_sample] += note_wave
            
        # Normalize
        max_val = np.max(np.abs(audio_data))
        if max_val > 0:
            audio_data /= max_val
            
        # Convert to 16-bit PCM
        audio_data_int16 = (audio_data * 32767).astype(np.int16)
        wavfile.write(wav_file, sample_rate, audio_data_int16)
        return wav_file

