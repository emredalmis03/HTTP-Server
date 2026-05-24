import os
from fastapi import FastAPI

app = FastAPI(title="devops-case-http-server")

BUILD_SHA = os.getenv("BUILD_SHA", "local")

@app.get("/ping")
def ping():
    return "pong"

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"build_sha": BUILD_SHA}
