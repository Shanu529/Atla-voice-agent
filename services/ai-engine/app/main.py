

from fastapi import FastAPI
from pydantic import BaseModel

app  = FastAPI(
    title = " ai engine",
)

class ChatRequest(BaseModel):
    message : str

class ChatResponse(BaseModel):
    response : str


@app.get("/healthy")

def healthy():
    return {"status" : "ok", "service" : "Ai Engine"}


@app.post("/chat", response_model=ChatResponse)
def chat(request : ChatRequest):
    return ChatResponse(
        response = f"AI engine received  : {request.message}"
    )
