# 🎵 From Code to Chords: Neural Melody Synthesis

> An LSTM-based deep learning system that generates and continues melodies from MIDI input — trained on 30,000+ folk songs from the Essen Folksong Collection.

---

## Overview

This project explores AI-driven music composition using Long Short-Term Memory (LSTM) networks. Given any MIDI file as input, the system encodes the melody into a symbolic time-series format, feeds it into a trained LSTM model, and generates a coherent musical continuation — which is then rendered as a MIDI file and visualized in MuseScore.

The goal is to democratize music composition: giving musicians, hobbyists, and educators an intelligent tool to explore new melodic ideas without requiring deep music theory knowledge.

---

## 💡 Why This Project?

Music generation is a complex sequence modeling problem.  
This project explores how LSTMs can learn temporal patterns in melodies and generate musically coherent continuations.

It demonstrates the application of deep learning to creative domains like music composition.

---

## 🎥 Demo

https://github.com/user-attachments/assets/f4a5aa7d-c2d5-4af2-8f9e-911143cf0414

---

## Features

- 🎼 Upload any MIDI file and get an AI-generated melodic continuation
- 🧠 LSTM model trained on 30,000+ German folk songs (Essen Folksong Collection)
- 🎛️ Temperature-based sampling for controlling creativity vs. structure
- 📄 Output rendered as sheet music in MuseScore Studio 4
- 🖥️ Clean Streamlit web interface — no CLI required
- ⚡ Fast generation without GPU requirement

---

## Tech Stack

| Category | Tools |
|---|---|
| Frontend | Streamlit |
| Deep Learning | TensorFlow 2.13, Keras |
| Music Processing | Music21 |
| Data Handling | NumPy, JSON |
| Visualization | MuseScore Studio 4 |
| Language | Python 3.8 |

---

## How It Works

1. **Preprocessing** — MIDI files are parsed and transposed to C Major/A Minor for consistency. Notes and rests are encoded into a symbolic time-series format:
   ```
   55 _ _ _ 57 _ _ 58 _ _ _ _ 60 _ _ _
   ```
   where integers are MIDI pitches, `_` means "hold note", and `r` is a rest.

2. **Training** — An LSTM model learns sequential patterns across 30,000+ encoded melodies, capturing pitch transitions, rhythm, and phrasing.

3. **Generation** — The uploaded MIDI is encoded as a seed and fed into the model. The model predicts the next note step-by-step using temperature sampling — balancing predictability with creativity.

4. **Output** — The generated sequence is decoded back into a MIDI file and opened in MuseScore for playback and sheet music visualization.

---

## Model Architecture

```
Input Layer     →  (None, 64, 38)      # Sequence of one-hot encoded notes
LSTM Layer      →  256 units           # Captures temporal dependencies
Dropout         →  0.2                 # Prevents overfitting  
Dense (Softmax) →  38 units            # Probability over note vocabulary

Total Parameters: 286,226 (1.09 MB)
```

The model was trained for 90 epochs with a batch size of 64, using sparse categorical crossentropy loss and the Adam optimizer (lr = 0.001).

---

## Setup Instructions

### Prerequisites
- Python 3.8
- MuseScore Studio 4 installed ([download here](https://musescore.org/))

### Installation

```bash
# Clone the repository
git clone https://github.com/shourya-mittal/melody-generator.git
cd melody-generator

# Create and activate a virtual environment
python -m venv myvenv
myvenv\Scripts\activate        # Windows
source myvenv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Configure MuseScore Path (one-time setup)

```bash
python -c "
import music21
music21.environment.set('musicxmlPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe')
music21.environment.set('musescoreDirectPNGPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe')
"
```

> Adjust the path if MuseScore is installed in a different location.

### Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Try It With Sample MIDI Files

The `uploaded_files/` directory includes several sample MIDI files to get started right away:

| File | Description |
|---|---|
| `sample.mid` | General test melody |
| `birthday.mid` | Simple, recognizable tune — great for first test |
| `MIDI 1.mid` | Short melodic phrase |
| `MIDI 2.mid` | Slightly longer sequence |

> **Tip:** Start with `birthday.mid` or `sample.mid` — short, clean melodies produce the best and most musically coherent continuations.

---

## Limitations

- Generates **monophonic** (single-note) melodies only — no chords or harmonies
- Trained predominantly on **folk music**, so outputs carry a folk/classical character regardless of input
- Works best with **simple, single-instrument MIDI** — complex multi-track files may yield inconsistent results
- No built-in tempo or key signature preservation from the input

---

## Future Scope

- Integrate transformer-based architectures (e.g., Music Transformer) for longer-range musical structure
- Real-time melody generation with in-app MIDI playback
- Support for multi-instrument and polyphonic generation
- Genre-specific models trained on jazz, classical, or pop datasets
- User-driven temperature control via the UI

---

## Project Structure

```
melody-generator/
│
├── app.py                  # Streamlit frontend
├── melodygenerator.py      # LSTM model + generation logic
├── preprocess.py           # MIDI encoding and dataset utilities
├── train.py                # Model training script
├── model.h5                # Pre-trained LSTM model
├── mapping.json            # Note-to-integer vocabulary mapping
├── file_dataset            # Encoded training dataset
├── requirements.txt
└── uploaded_files/         # Sample MIDI files for testing
```

---

## References

1. Subramanian et al. (2023) — *Deep Learning Approaches for Melody Generation: LSTM, BiLSTM and GRU*
2. Fathima et al. (2024) — *Neural Harmony: Advancing Composition with RNN-LSTM*
3. Dong (2023) — *Using deep learning and genetic algorithms for melody generation*
4. Briot (2021) — *From artificial neural networks to deep learning for music generation*
5. Wu et al. (2020) — *A hierarchical recurrent neural network for symbolic melody generation*
6. Graves (2013) — *Generating Sequences With Recurrent Neural Networks*

---

## 👨‍💻 Author

**Shourya Mittal**  
📧 shouryamittal2004@gmail.com
