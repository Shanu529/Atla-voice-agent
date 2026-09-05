import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from app.tools import TOOLS


load_dotenv()


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL = os.getenv("GROQ_MODEL")


tool_definitions = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local time.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_date",
            "description": "Get today's date.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "open_application",
            "description": "Open an installed application such as Chrome, Notepad, Calculator, Explorer, or VS Code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "application": {
                        "type": "string",
                        "description": "Application to open.",
                    }
                },
                "required": ["application"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "open_website",
            "description": "Open a website in the user's browser.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "Website URL.",
                    }
                },
                "required": ["url"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": "List files and folders inside a directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Directory path.",
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a text file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file.",
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Create a new empty file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path of the new file.",
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_system_info",
            "description": "Get basic computer system information.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the internet for current information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query.",
                    }
                },
                "required": ["query"],
            },
        },
    },
{
    "type": "function",
    "function": {
        "name": "create_folder",
        "description": "Create a folder on the computer.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path of the folder to create.",
                }
            },
            "required": ["path"],
        },
    },
},

{
    "type": "function",
    "function": {
        "name": "get_special_folder",
        "description": "Resolve a common folder such as Downloads, Desktop, Documents, Pictures, or Videos.",
        "parameters": {
            "type": "object",
            "properties": {
                "folder": {
                    "type": "string",
                    "description": "Folder name such as downloads, desktop, documents, pictures, or videos.",
                }
            },
            "required": ["folder"],
        },
    },
},


{
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write text content to a file. Use this when the user asks to create or modify a file with specific content.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "The path of the file to write"
                },
                "content": {
                    "type": "string",
                    "description": "The complete content to write into the file"
                }
            },
            "required": ["path", "content"]
        }
    }
},

]


def chat(message: str) -> str:

    messages = [
        {
            "role": "system",
            "content": (
                "You are Atla, a desktop AI assistant.\n"
                "Use search_web when the user asks to search, research, "
                "look up, or find information on the internet.\n"
                "Use open_website ONLY when the user explicitly asks you "
                "to open or visit a website.\n"
                "Use open_application ONLY when the user explicitly asks "
                "to open or launch an application.\n"
                "Use filesystem tools when the user asks you to work with "
                "files or folders. Use get_special_folder when the user "
                "refers to common folders such as Desktop or Downloads.\n"
                "You may use multiple tools when necessary.\n"
                "Never claim an action succeeded unless the tool reports success."
            ),
        },
        {
            "role": "user",
            "content": message,
        },
    ]

    while True:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tool_definitions,
            tool_choice="auto",
        )

        assistant_message = response.choices[0].message

        # LLM has finished and doesn't need another tool.
        if not assistant_message.tool_calls:

            return assistant_message.content or ""

        # Save the LLM's tool request.
        messages.append(assistant_message)

        # Execute every requested tool.
        for tool_call in assistant_message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments or "{}"
            )

            tool = TOOLS.get(tool_name)

            if not tool:
                result = f"Unknown tool: {tool_name}"

            else:
                try:
                    result = tool(**arguments)

                except Exception as e:
                    result = f"Tool failed: {e}"

            # Send tool result back to the LLM.
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result),
                }
            )


