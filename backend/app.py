from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from cv_engine import load_image_bytes, analyze_cv
from ai_engine import try_gemini, try_openai
from utils import to_base64
from report_generator import build_pdf
from models import InspectionResult, Defect
import base64

app = FastAPI(title="TaurgoVision - Full Option X")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    b = await file.read()
    img = load_image_bytes(b)

    ai = try_gemini(b) or try_openai(b)
    if ai:
        ai["original_image"] = None
        ai["overlay_image"] = None
        return ai

    defects, summary, recs, overlay = analyze_cv(img)

    return {
        "defects": defects,
        "summary": summary,
        "recommendations": recs,
        "original_image": to_base64(img),
        "overlay_image": to_base64(overlay)
    }

@app.post("/pdf")
async def pdf(result: InspectionResult):
    pdf_bytes = build_pdf(result)
    return {"pdf": base64.b64encode(pdf_bytes).decode()}