import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from app.tools import get_current_time


load_dotenv()


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL = os.getenv("GROQ_MODEL")


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    }
]


def chat(message: str) -> str:

    messages = [
        {
            "role": "user",
            "content": message,
        }
    ]

    # First ask the LLM what to do.
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
    )

    assistant_message = response.choices[0].message

    # No tool needed.
    if not assistant_message.tool_calls:
        return assistant_message.content or ""

    print("CONTENT:", assistant_message.content)
    print("TOOL CALLS:", assistant_message.tool_calls)


    # Add the assistant's tool request to the conversation.
    messages.append(assistant_message)

    for tool_call in assistant_message.tool_calls:

        tool_name = tool_call.function.name

        if tool_name == "get_current_time":

            result = get_current_time()

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                }
            )

    # Ask the LLM again using the tool result.
    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
    )

    return final_response.choices[0].message.content or ""