

# pip install scipy

from http import client

import sounddevice as sd
from scipy.io.wavfile import write


SAMPLE_RATE = 16000
RECORD_SECONDS = 5


def record_audio(filename="input.wav"):
    print(" Speak now...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        device=2,
    )

    sd.wait()

    write(filename, SAMPLE_RATE, audio)

    print(f"Audio saved: {filename}")



def transcribe_audio(filename="input.wav"):
    with open(filename, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-large-v3-turbo", file=audio_file
        )
    return transcript.text





if __name__ == "__main__":
    record_audio()

    text = transcribe_audio()

    print(f"Transcribed text: {text}")

