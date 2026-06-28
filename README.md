# AI Multilingual Voice & Text Summarizer

## Overview

AI-powered multilingual summarization application built using Hugging Face Transformers, Whisper, Google Translate, gTTS, and Streamlit.

The application can process text files, PDF documents, and audio files, generate summaries, translate content between languages, and provide audio playback of the generated summary.

---

## Features

* TXT file summarization
* PDF document summarization
* Audio-to-text transcription using Whisper
* Multi-language translation
* Long-text chunking support
* Hugging Face Transformer summarization
* Text-to-speech summary generation
* Audio playback inside Streamlit
* Download summary as text file

---

## Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* Whisper
* Google Translate API
* gTTS
* PyPDF2
* FFmpeg

---

## Project Structure

Text-Summarization-GenAI/

├── app.py

├── summarizer.py

├── audio_utils.py

├── utils.py

├── requirements.txt

├── README.md

├── sample_text.txt

---

## Installation

### Clone Repository

git clone <repository-url>

cd Text-Summarization-GenAI

### Install Dependencies

pip install -r requirements.txt

### Install FFmpeg

Download FFmpeg and add it to your system PATH.

Verify installation:

ffmpeg -version

---

## Run Application

streamlit run app.py

---

## Usage

### Text Input

1. Select Text/PDF mode
2. Upload a TXT file
3. Click Generate Summary

### PDF Input

1. Select Text/PDF mode
2. Upload a PDF file
3. Click Generate Summary

### Audio Input

1. Select Audio mode
2. Upload an audio file (.mp3, .wav, .m4a)
3. Choose output language
4. Generate translated summary
5. Listen to generated audio output

<img width="1137" height="906" alt="img1" src="https://github.com/user-attachments/assets/89e15c44-6099-4e2d-8f25-d4afe4400f45" />

<img width="997" height="904" alt="img2" src="https://github.com/user-attachments/assets/d66cf4e8-5ed9-4efb-b962-b252a593f3eb" />

<img width="897" height="916" alt="img3" src="https://github.com/user-attachments/assets/7362011e-c2b1-410b-97ae-15ba9291b72a" />
