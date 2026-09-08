from stt import listen
from agent_client import send_to_agent
from tts import speak


def run_voice_assistant():
    print(" Atla is ready. Say 'exit' to stop.")

    while True:
        text = listen()

        text = text.strip()

        if not text:
            print("Nothing heard. Listening again...")
            continue

        print(f" You said: {text}")

        if text.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye.")
            break

        reply = send_to_agent(text)

        print(f" Atla: {reply}")

        speak(reply)


if __name__ == "__main__":
    
    run_voice_assistant()