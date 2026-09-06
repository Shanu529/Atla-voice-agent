import requests


AGENT_SERVICE_URL = "http://localhost:8081/chat"


def send_to_agent(message: str) -> str:
    response = requests.post(
        AGENT_SERVICE_URL,
        json={"message": message},
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    return data["reply"]