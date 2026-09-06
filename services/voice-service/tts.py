import pyttsx3


def speak(text: str):
    engine = pyttsx3.init("sapi5")

    voices = engine.getProperty("voices")

    # Microsoft David
    engine.setProperty("voice", voices[0].id)

    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":
    speak("Hello Shanu . I am Atla. How can I help you?")