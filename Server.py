import os
from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

N8N_BASE_URL = os.getenv("N8N_BASE_URL", "http://127.0.0.1:5678").rstrip("/")
START_INTERVIEW_PATH = os.getenv("N8N_START_WEBHOOK_PATH", "/webhook-test/start-interview")
ANSWER_PATH = os.getenv("N8N_ANSWER_WEBHOOK_PATH", "/webhook-test/interview-turn")

@app.get("/", response_class=HTMLResponse)
def serve_html():
    try:
        with open("Mock_Interviewer.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: Mock_Interviewer.html not found."

@app.post("/api/start-interview")
def proxy_start_interview(data: UploadFile = File(...)):
    files = {"data": (data.filename, data.file, data.content_type)}
    response = requests.post(f"{N8N_BASE_URL}{START_INTERVIEW_PATH}", files=files, timeout=60)
    return response.json()

@app.post("/api/answer")
def proxy_answer(session_id: str = Form(...), audio: Optional[UploadFile] = File(None)):
    payload = {"session_id": session_id}

    if audio and audio.filename:
        files = {"audio": (audio.filename, audio.file, audio.content_type)}
        response = requests.post(f"{N8N_BASE_URL}{ANSWER_PATH}", files=files, data=payload, timeout=60)
    else:
        response = requests.post(f"{N8N_BASE_URL}{ANSWER_PATH}", data=payload, timeout=60)

    return response.json()