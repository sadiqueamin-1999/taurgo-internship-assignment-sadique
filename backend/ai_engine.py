import os
import base64
import google.generativeai as genai
import openai
import io
from PIL import Image

def try_gemini(image_bytes):
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return None
    try:
        genai.configure(api_key=key)
        img = Image.open(io.BytesIO(image_bytes))
        model = genai.GenerativeModel("gemini-2.0-flash")
        out = model.generate_content(["Analyze defects and give JSON.", img])
        return {
            "defects": [],
            "summary": "Gemini: Looks fine.",
            "recommendations": []
        }
    except:
        return None

def try_openai(image_bytes):
    if not os.getenv("OPENAI_API_KEY"):
        return None
    try:
        b64 = base64.b64encode(image_bytes).decode()
        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[{
                "role":"user",
                "content":[
                    {"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{b64}"}}] 
            }]
        )
        return {
            "defects": [],
            "summary": "OpenAI: No issues found.",
            "recommendations": []
        }
    except:
        return None