import music21
from music21 import note, stream
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# Define a list of notes
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

# Map notes to integers
note_to_int = {note: i for i, note in enumerate(notes)}
int_to_note = {i: note for i, note in enumerate(notes)}

# Generate training data
X = []
y = []
for i in range(1000):
    sequence = np.random.choice(notes, size=10)
    X.append([note_to_int[n] for n in sequence])
    y.append(note_to_int[np.random.choice(notes)])

X = np.array(X)
y = np.array(y)

# Reshape X for LSTM
X = X.reshape(X.shape[0], X.shape[1], 1)

# Build model
model = Sequential()
model.add(LSTM(64, input_shape=(X.shape[1], 1)))
model.add(Dropout(0.2))
model.add(Dense(len(notes), activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train model
model.fit(X, y, epochs=100, batch_size=32)

# Generate music
def generate_music(length):
    sequence = np.random.choice(notes, size=10)
    generated_music = []
    for _ in range(length):
        x = np.array([note_to_int[n] for n in sequence]).reshape(1, 10, 1)
        prediction = model.predict(x)
        predicted_note = int_to_note[np.argmax(prediction[0])]
        generated_music.append(predicted_note)
        sequence = np.append(sequence[1:], predicted_note)
    return generated_music

# Create music21 stream
def create_stream(music):
    stream1 = stream.Stream()
    for n in music:
        stream1.append(note.Note(n))
    return stream1

# Generate and save music
music = generate_music(100)
stream1 = create_stream(music)
stream1.write('midi', fp='generated_music.mid')

print("Music generated and saved to generated_music.mid")
