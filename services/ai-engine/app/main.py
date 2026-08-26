

from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

from app.agent import run_agent

load_dotenv()


app  = FastAPI(
    title = " ai engine",
)

class ChatRequest(BaseModel):
    message : str

class ChatResponse(BaseModel):
    reply : str


@app.get("/health")

def healthy():
    return {"status" : "ok", "service" : "Ai Engine"}




@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request : ChatRequest):

    reply = run_agent(request.message)
    return ChatResponse(
        reply = reply
    )
