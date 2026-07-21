from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

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
    # Use /webhook/ if active in n8n, or /webhook-test/ while testing node-by-node
    n8n_url = "http://127.0.0.1:5678/webhook-test/start-interview"
    response = requests.post(n8n_url, files=files)
    return response.json()

@app.post("/api/answer")
def proxy_answer(session_id: str = Form(...), audio: Optional[UploadFile] = File(None)):
    payload = {"session_id": session_id}
    n8n_url = "http://127.0.0.1:5678/webhook-test/interview-turn"
    
    # If audio is sent (Loop turn), forward files + payload
    if audio and audio.filename:
        files = {"audio": (audio.filename, audio.file, audio.content_type)}
        response = requests.post(n8n_url, files=files, data=payload)
    else:
        # If no audio is sent (Initial turn), forward ONLY payload
        response = requests.post(n8n_url, data=payload)
        
    return response.json()