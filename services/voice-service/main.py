

from stt import listen
from agent_client import send_to_agent


def run_voice_command():
    text = listen()

    print(f" You said: {text}")

    reply = send_to_agent(text)

    print(f" Atla: {reply}")


if __name__ == "__main__":
    run_voice_command()