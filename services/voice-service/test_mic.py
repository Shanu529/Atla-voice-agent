


import sounddevice as sd

print("Recording for 5 seconds... Speak now!")

audio = sd.rec(
    int(5 * 16000),
    samplerate=16000,
    channels=1,
    dtype="int16",
    device=2,
)

sd.wait()

print("Recording finished.")