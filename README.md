
# YouTube AI Summarizer

**YouTube AI Summarizer** is a Python-based tool designed to extract audio from YouTube videos, transcribe the audio into text, and summarize the content using AI models. The tool provides an efficient way to quickly grasp the key points of a video without having to watch it in full.

## Project Overview

This project leverages the following technologies:

- **yt-dlp**: A command-line tool that extracts audio from YouTube videos.
- **Whisper by OpenAI**: A deep learning-based automatic speech recognition (ASR) model used to transcribe the audio into text.
- **BART (facebook/bart-large-cnn)**: A transformer model from Hugging Face used to summarize the transcribed text.

The goal of this project is to enable users to:
1. Automatically download the audio from YouTube videos.
2. Convert the audio to text.
3. Generate a concise summary of the transcribed text, making it easier to understand and digest the content of videos.

## Features

- **Audio Extraction**: Extracts audio from YouTube videos in high quality.
- **Speech-to-Text**: Uses Whisper to convert the extracted audio into text.
- **Text Summarization**: Uses the BART model to generate a short summary of the transcribed text.
- **Easy-to-Use**: Simply input the YouTube video URL to get a summarized output.

## Requirements

Before running the script, ensure that the following dependencies are installed:

- Python 3.7 or higher
- `yt-dlp`: For downloading and extracting audio from YouTube videos.
- `whisper`: For speech-to-text transcription.
- `transformers`: For text summarization using Hugging Face models.
- FFmpeg: A multimedia framework required for audio extraction.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/YouTube-AI-Summarizer.git
   cd YouTube-AI-Summarizer
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the necessary libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**:
   You will need to have FFmpeg installed to process the audio. Download FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.

## Usage

1. Run the script:

    ```bash
    python youtubeAisummarizer.py
    ```

2. When prompted, enter the URL of the YouTube video you want to summarize:
    ```bash
    please enter youtube video link: https://www.youtube.com/watch?v=VIDEO_ID
    ```

3. The program will:
   - Extract the audio from the YouTube video.
   - Transcribe the audio into text.
   - Summarize the transcribed text using a pre-trained BART model.
   - Print the summary of the video.

### Example:

```bash
please enter youtube video link: https://www.youtube.com/watch?v=BtN-goy9VOY
Extracting audio...
Transcribing audio...
Summarizing text...
Summary of the video:
This video explains the importance of self-awareness in personal growth. It discusses the benefits of reflection and how understanding one's strengths and weaknesses can lead to better decision-making and a more fulfilling life.
```

## How It Works

1. **Audio Extraction**: 
   - The script uses `yt-dlp` to download the best available audio from the provided YouTube URL. This audio is then saved as an `.mp3` file.
   
2. **Transcription**:
   - The `whisper` model processes the downloaded audio and transcribes it into text. Whisper uses advanced deep learning techniques to recognize and convert speech into written words.
   
3. **Summarization**:
   - The transcribed text is then passed to the Hugging Face `transformers` library, where the BART model is used to generate a concise summary. BART is a powerful text generation model that excels in summarization tasks.

## Troubleshooting

- **FFmpeg Not Found**: Ensure that FFmpeg is installed and added to your system's PATH. 
- **Long Transcriptions**: If the transcribed text is very long, you may want to adjust the summarizer settings to fit within the model's input length.
