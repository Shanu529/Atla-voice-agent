

from fastapi import FastAPI

app  = FastAPI(
    title = " ai engine",
)


@app.get("/healty")

def healthy():
    return {"status" : "ok", "service" : "Ai Engine"}