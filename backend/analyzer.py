import numpy as np
import cv2
from pillow_heif import register_heif_opener
from PIL import Image
import io

register_heif_opener()

def load_image_bytes(image_bytes: bytes):
    """Loads JPG/PNG/HEIC into RGB numpy array."""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    return np.array(img)

def analyze_cv(img):
    """Simple CV-based defect signal: edge density."""
    edges = cv2.Canny(img, 80, 160)
    intensity = int(edges.sum())

    defects = []
    summary = "No major defects detected."
    recs = ["No urgent action required."]

    if intensity > 50000:
        defects.append({
            "type": "Surface Crack",
            "severity": "Moderate",
            "confidence": 0.79,
            "notes": "High edge density suggests cracking."
        })
        summary = "Cracking possibly detected."
        recs = ["Consider manual inspection."]

    return defects, summary, recs