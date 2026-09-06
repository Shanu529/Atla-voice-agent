import os

import sounddevice as sd
from scipy.io.wavfile import write
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


SAMPLE_RATE = 16000
RECORD_SECONDS = 5
MICROPHONE_DEVICE = 2


def record_audio(filename="input.wav"):
    print(" Speak now...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        device=MICROPHONE_DEVICE,
    )

    sd.wait()

    write(filename, SAMPLE_RATE, audio)

    print(f"Audio saved: {filename}")


def transcribe_audio(filename="input.wav"):
    with open(filename, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=audio_file,
        )

    return transcript.text


def listen():
    record_audio()
    return transcribe_audio()


if __name__ == "__main__":
    text = listen()

    print(f"📝 Transcribed text: {text}")