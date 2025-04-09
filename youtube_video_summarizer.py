'''
extract audio 
convert it to text 
summerize it using Ai
'''
import yt_dlp 
from io import BytesIO
import subprocess
import whisper 
from transformers import pipeline
import tempfile


audio_file=BytesIO()

def convert_to_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # This chooses the best available audio format
        'outtmpl': 'audio.%(ext)s',  # This defines the name of the output file (audio.mp3 or audio.webm)
        'quiet': True,               # Suppress unnecessary output to make the process quieter
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # This tells yt-dlp to convert the downloaded audio file
            'preferredcodec': 'mp3',  # Converts the audio to mp3 format (can be 'wav', 'aac', etc.)
            'preferredquality': '192',  # Audio quality, you can adjust this to 128, 320, etc.
        }]
        
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
     # Extract video info (no download yet)
         meta_data = ydl.extract_info(url, download=False)
         process = subprocess.Popen(
            ['yt-dlp', '-f', 'bestaudio', '--extract-audio', '--audio-format', 'mp3', '-o', '-', url],
            stdout=subprocess.PIPE,  # Pipe the stdout (audio) to memory
            stderr=subprocess.PIPE
        )
         audio_file.write(process.stdout.read()) 
         audio_file.seek(0)

         # Save BytesIO content to a temp file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            temp_file.write(audio_file.getvalue())
            temp_audio_path = temp_file.name
    return temp_audio_path


def audio_to_text(temp_audio_path):
     model = whisper.load_model("base")
     result = model.transcribe(temp_audio_path)
     text_file=result["text"]
     return text_file

def  Summarizing_the_text(text_file):
     words = text_file.split()
     max_len= min(512, int(len(words) * 0.5)) 
     min_len=max(30, int(len(words) * 0.2))
     print(f"Summarizing with max_length={max_len}, min_length={min_len}")
     summarizer = pipeline("summarization", model="facebook/bart-large-cnn") # loads a pre-trained model suitable for text summarization.
     summary=summarizer(text_file,max_length=max_len,min_length=min_len)  
     summary_text = summary[0]['summary_text'] 
     return summary_text
     '''
     summarizer returns the summary as a list of dictionaries,
     where each dictionary contains a summary_text key, which holds the generated summary.
     thats why i used index 0
     '''
def summarize_youtube_video(url):
    print("Extracting audio...")
    audio = convert_to_audio(url)  
    
    print("Transcribing audio...")
    transcription = audio_to_text(audio)
    
    print("Summarizing text...")
    summary = Summarizing_the_text(transcription) 
    
    print("\nSummary of the video:\n", summary)

if __name__=="__main__":
     url=input("please enter youtube video link: ")
     summarize_youtube_video(url)





     
     


