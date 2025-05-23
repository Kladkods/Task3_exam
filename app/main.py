
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Firebase!"}

@app.get("/health")
def health():
    return {"status": "ok"}
