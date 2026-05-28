import os
from music21 import stream, note, chord, duration

data_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(data_dir, exist_ok=True)

def generate_chords():
    """Generates a MIDI file containing chord progressions."""
    s = stream.Stream()
    
    # C major (C-E-G), G major (G-B-D), A minor (A-C-E), F major (F-A-C)
    progressions = [
        [60, 64, 67], [59, 62, 67], [57, 60, 64], [53, 57, 60], # Progression 1
        [60, 64, 67], [53, 57, 60], [55, 59, 62], [60, 64, 67], # Progression 2
        [57, 60, 64], [53, 57, 60], [60, 64, 67], [59, 62, 67]  # Progression 3
    ]
    
    # Repeat to make the file richer
    for _ in range(4):
        for chord_pitches in progressions:
            c = chord.Chord(chord_pitches)
            c.duration = duration.Duration(1.0) # 1 beat
            s.append(c)
            
    output_path = os.path.join(data_dir, "chords_progression.mid")
    s.write('midi', fp=output_path)
    print(f"Generated: {output_path}")

def generate_melody():
    """Generates a MIDI file containing a melodic motif."""
    s = stream.Stream()
    
    # Some melodic leaps and step-wise movements in C major/A minor
    melody_pitches = [
        60, 62, 64, 67, 69, 67, 64, 60,
        64, 67, 72, 71, 69, 67, 64, 62,
        60, 57, 60, 64, 67, 64, 60, 57,
        55, 57, 59, 60, 62, 64, 59, 60
    ]
    
    for _ in range(4):
        for pitch in melody_pitches:
            n = note.Note(pitch)
            # Alternate note durations for rhythmic diversity
            n.duration = duration.Duration(0.5 if pitch % 2 == 0 else 0.25)
            s.append(n)
            
    output_path = os.path.join(data_dir, "melody_pattern.mid")
    s.write('midi', fp=output_path)
    print(f"Generated: {output_path}")

def generate_arpeggios():
    """Generates a MIDI file containing rising and falling arpeggios."""
    s = stream.Stream()
    
    # Arpeggios: C major, A minor, D minor, G major
    arp_patterns = [
        [60, 64, 67, 72, 67, 64], # C Major
        [57, 60, 64, 69, 64, 60], # A Minor
        [59, 62, 67, 74, 67, 62], # G Major
        [53, 57, 60, 65, 60, 57]  # F Major
    ]
    
    for _ in range(4):
        for pattern in arp_patterns:
            for pitch in pattern:
                n = note.Note(pitch)
                n.duration = duration.Duration(0.25) # 16th notes
                s.append(n)
                
    output_path = os.path.join(data_dir, "minor_scale_arpeggios.mid")
    s.write('midi', fp=output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    generate_chords()
    generate_melody()
    generate_arpeggios()
