

from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

from app.llm import chat

load_dotenv()


print(chat("hi how are you"))
app  = FastAPI(
    title = " ai engine",
)

class ChatRequest(BaseModel):
    message : str

class ChatResponse(BaseModel):
    response : str


@app.get("/health")

def healthy():
    return {"status" : "ok", "service" : "Ai Engine"}




# @app.post("/chat", response_model=ChatResponse)
# def chat(request : ChatRequest):
#     return ChatResponse(
#         response = f"AI engine received  : {request.message}"
#     )
