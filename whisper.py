import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe_audio(path):
    with open(path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file)

    with open("./results/transcription.txt", "w") as transcription_file:
        transcription_file.write(transcript.text)

    print("Transcription Done!!")


transcribe_audio("./bin/audio.mp3")
