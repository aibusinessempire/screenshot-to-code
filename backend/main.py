from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.post("/chat")
async def chat(message: str):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)
    return {"reply": response.text}
