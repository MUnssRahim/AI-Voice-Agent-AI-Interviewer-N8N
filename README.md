#PROJECT DEMO :
https://drive.google.com/file/d/1fpyyhkNN7HdJkT3s3unbXFBVZkGQFFOd/view?usp=drivesdk



# AI Mock Interviewer

AI Mock Interviewer is a voice-first mock interview system that turns a candidate's resume into a personalized technical interview experience. It combines a simple web interface, a FastAPI backend, an n8n workflow, and AI services for speech-to-text, text-to-speech, and question generation.

The goal is simple: make interview practice feel closer to a real engineering conversation instead of a generic questionnaire.

---

## What this project does

This project lets a user:

- upload a resume in PDF format,
- generate a tailored interview script from the resume content,
- receive questions one at a time in a voice-based flow,
- answer with microphone input,
- continue the interview in a conversational loop.

It is designed for students, job seekers, and engineers who want to practice technical interviews in a more realistic and adaptive way.

---

## Why this project is useful

Most mock interview tools ask the same broad questions. This one tries to be more thoughtful.

Instead of asking random interview questions, it uses the resume as the source of truth and builds questions around:

- the skills the candidate actually claims,
- the projects they mention,
- the real engineering trade-offs they would likely be asked about,
- practical interview situations that sound natural when spoken aloud.

That makes the experience more relevant and more useful for preparation.

---

## Project structure

- [Server.py](Server.py) – FastAPI server that serves the web app and forwards requests to the n8n workflow.
- [Mock_interviewer.html](Mock_interviewer.html) – Frontend interface for uploading a resume, starting the interview, and recording answers.
- [AI_Mock_Interviewer.json](AI_Mock_Interviewer.json) – n8n workflow containing the interview logic, prompt design, and AI integrations.

---

## How it works

1. The user uploads a resume PDF through the web interface.
2. The FastAPI server forwards the file to an n8n webhook.
3. The workflow extracts the resume text and sends it to an LLM.
4. The LLM generates a structured interview script with:
   - behavioral questions,
   - project-based questions,
   - technical questions tied to the candidate's listed skills.
5. The first question is sent back to the browser.
6. The browser plays the question as audio and lets the user respond through the microphone.
7. The answer is transcribed, stored in the session flow, and the next question is generated.

---

## Main components

### 1. Frontend

The frontend is a polished single-page experience that provides:

- resume upload,
- interview session state,
- question display,
- microphone-based answer recording,
- animated audio status UI.

### 2. Backend

The backend is a lightweight FastAPI app that:

- serves the HTML interface,
- accepts resume upload requests,
- forwards requests to n8n webhooks.

### 3. n8n workflow

The workflow is the main intelligence layer. It handles:

- resume parsing,
- interview prompt construction,
- LLM-based question generation,
- speech-to-text,
- text-to-speech,
- session state transitions.

### 4. AI services

The workflow uses AI services to make the experience interactive:

- LLM for generating interview questions,
- speech-to-text for transcribing spoken answers,
- text-to-speech for reading questions aloud.

---

## Interview prompt design

The core prompt is built around a strong idea: the interview should feel like a serious engineering conversation, not a random chatbot quiz.

The prompt instructs the model to:

- analyze the resume first,
- prioritize the candidate's stated technical skills,
- build questions around actual experience,
- avoid generic or invented scenarios,
- keep questions natural for spoken delivery,
- test practical engineering trade-offs,
- return output as strict JSON.

### Prompt principles

The prompt has four major design pillars:

1. Resume-first alignment
   - Every question should connect directly to something the candidate actually listed.
   - This keeps the interview grounded and relevant.

2. Voice-optimized rigor
   - Questions are written to sound natural when read aloud.
   - They are deep, precise, and easy to understand in spoken form.

3. Engineering reality
   - The questions push the candidate to explain trade-offs, constraints, and technical decisions.
   - This is important because real interviews are rarely about memorizing facts; they are about judgment.

4. Structured output
   - The model must return a clean JSON object.
   - That makes it easy for the workflow to use the questions programmatically.

---

## Why the prompt is efficient and strong

This prompt works well because it does three things very effectively:

- It stays grounded in reality.
  The interviewer does not rely on fake or unrelated scenarios. It uses the resume as its anchor.

- It is structured for execution.
  The prompt is not only good for generating questions; it is also good for automation because it forces a predictable output format.

- It balances depth and practicality.
  The questions are challenging, but they are still realistic and usable in a voice-based interview experience.

In short, the prompt is strong because it is not just trying to generate "smart-looking" questions. It is trying to generate useful questions that reflect the candidate's background and test actual engineering thinking.

---

## What this interviewer is based on

This interviewer is based on a practical interview framework that combines:

- resume-driven questioning,
- technical depth,
- project-based analysis,
- behavioral reasoning,
- voice-first interaction.

It reflects the style of a good engineering interview where the interviewer does not simply ask, "Tell me about yourself." Instead, they ask things like:

- How would you justify this design choice under real constraints?
- What trade-offs did you consider in this project?
- How would you handle scaling, latency, accuracy, or reliability issues?

That is the spirit of this project.

---

## Setup instructions

### Prerequisites

You will need:

- Python 3.9+
- FastAPI
- Uvicorn
- requests
- python-multipart
- an n8n instance
- access to AI services such as Groq or similar providers
- optional: Supabase for session persistence

### Install Python dependencies

```bash
pip install fastapi uvicorn requests python-multipart
```

### Start the backend

From the project root, run:

```bash
uvicorn Server:app --reload --host 0.0.0.0 --port 8000
```

Then open the app in your browser at:

```text
http://127.0.0.1:8000/
```

### Set up n8n

1. Start your n8n instance.
2. Import the workflow from [AI_Mock_Interviewer.json](AI_Mock_Interviewer.json).
3. Make sure the workflow is active.
4. Ensure the webhook endpoints used by the FastAPI app are reachable.

### Configure your AI services

The workflow expects API credentials and service integrations to be configured in your environment. Make sure you have valid credentials for the AI providers you are using.

> Keep secrets private and never commit credentials, API keys, or private webhook URLs to version control.

---

## Usage flow

1. Open the web interface.
2. Upload a resume PDF.
3. Start the interview session.
4. Wait for the first question to appear.
5. Click the recording button and answer the question out loud.
6. Continue through the flow until the interview completes.

---

## Notes for students and early engineers

This project is a strong example of how to combine:

- frontend interaction,
- backend orchestration,
- AI prompt engineering,
- workflow automation,
- real-time audio processing.

It is especially useful as a learning project because it shows how a modern AI app can connect several systems together in a practical way.

---

## What I would improve next

If this project were extended further, the next valuable improvements would be:

- better session management,
- stronger answer evaluation,
- more detailed interviewer memory,
- better error handling for audio and transcription failures,
- a smoother multi-turn conversation experience,
- a dashboard for interview analytics.

---

## Summary

AI Mock Interviewer is a resume-driven, voice-first interview practice tool that tries to make mock interviews feel more realistic and more useful. Its main strength is that it does not ask generic questions. It uses the candidate's own background as the foundation for a deeper technical conversation.

That makes it a strong example of an AI-powered interviewer that is practical, structured, and meaningful.
