import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"


uvicorn.run(app, host="127.0.0.1", port=8003)
