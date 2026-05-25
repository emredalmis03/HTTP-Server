import json
import logging
import os
import time
import uuid

from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator

BUILD_SHA = os.getenv("BUILD_SHA", "local-dev")


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
        }

        if hasattr(record, "request_id"):
            log_record["request_id"] = record.request_id

        if hasattr(record, "method"):
            log_record["method"] = record.method

        if hasattr(record, "path"):
            log_record["path"] = record.path

        if hasattr(record, "status_code"):
            log_record["status_code"] = record.status_code

        if hasattr(record, "duration_ms"):
            log_record["duration_ms"] = record.duration_ms

        return json.dumps(log_record)


logger = logging.getLogger("devops-case")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logger.addHandler(handler)

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())

    start_time = time.time()

    response = await call_next(request)

    duration_ms = round((time.time() - start_time) * 1000, 2)

    logger.info(
        "request_completed",
        extra={
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
        },
    )

    response.headers["X-Request-ID"] = request_id

    return response


@app.get("/ping")
def ping():
    return "pong"


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"build_sha": BUILD_SHA}


Instrumentator().instrument(app).expose(app)
