# 🎤 Speech Emotion Recognition (SER) using NLP

This project detects **human emotions from real-time speech input** using **Natural Language Processing (NLP)** techniques. It captures the user's audio, converts it to text using speech recognition, and then performs **emotion analysis** on the transcribed text.

The goal is to provide an intuitive and interactive way to understand a speaker's emotional state through their spoken language.

---

## 🔍 Features

- 🎙️ Real-time audio capture
- 🗣️ Speech-to-text transcription using `SpeechRecognition`
- 💬 Emotion analysis using NLP sentiment/emotion models
- 📊 Outputs predicted emotion (e.g., Happy, Sad, Angry, Neutral)
- 🧪 Simple, extensible, and lightweight design

---

## 🧠 Tech Stack

- **Python 3**
- **SpeechRecognition** – for speech-to-text
- **PyAudio** – for capturing microphone input
- **Transformers / NLTK / TextBlob** – for NLP emotion analysis (based on your choice)
- **Matplotlib / Streamlit (optional)** – for GUI or visualization

---

## 🚀 How It Works

1. The user speaks into the microphone.
2. The system converts the audio to text.
3. The text is passed to a sentiment/emotion classifier.
4. The detected emotion is displayed to the user.

---

Make sure you have Python 3.7 or above installed.

