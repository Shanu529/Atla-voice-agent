

# pip install scipy

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


if __name__ == "__main__":
    record_audio()