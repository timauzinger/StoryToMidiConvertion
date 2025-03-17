import csv
from mido import Message, MidiFile, MidiTrack
import re  # For handling note parsing

# !!! Change ths Variable to match your generated CSV-Table !!!

INPUT_TABLE = "exampleStoryInterpretation.csv"

# Load word-note mapping from CSV
word_note_mapping = []

with open(INPUT_TABLE, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract main note, duration, and velocity (no chords yet)
        word_note_mapping.append((
            row["word"],
            row["note"],
            int(row["duration"]),
            int(row["velocity"])
        ))


# Function to convert note names (e.g., "C4", "C#4") to MIDI numbers
def note_to_midi(note):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5,
        'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }

    # Extract the note and octave
    import re
    match = re.match(r"([A-Ga-g#b]+)(\d+)$", note)

    if match:
        key = match.group(1)  # Extracts "C", "D#", "Bb", etc.
        octave = int(match.group(2))  # Extracts "4", "5", etc.
    else:
        raise ValueError(f"Invalid note format: {note}")

    if key not in note_map:
        raise ValueError(f"Unknown note: {key}")  # Debugging step

    return 12 * (octave + 1) + note_map[key]  # Convert to MIDI number


# Create MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Convert words into MIDI sequence (single notes only for now)
for word, note, duration, velocity in word_note_mapping:
    midi_note = note_to_midi(note)

    # Play the note
    track.append(Message('note_on', note=midi_note, velocity=velocity, time=0))

    # Release the note after the specified duration
    track.append(Message('note_off', note=midi_note, velocity=velocity, time=duration))

# Save MIDI file
filename = INPUT_TABLE.split(".")[0] + ".mid"
mid.save(filename)
print(f"MIDI file {filename} has been saved!")
