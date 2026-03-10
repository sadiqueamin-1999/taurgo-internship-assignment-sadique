import numpy as np
import cv2
from pillow_heif import register_heif_opener
from PIL import Image
import io

register_heif_opener()

def load_image_bytes(b: bytes):
    pil = Image.open(io.BytesIO(b)).convert("RGB")
    return np.array(pil)

def draw_overlays(img, cracks, damp):
    overlay = img.copy()

    # --- CRACK LINES (RED with BLACK outline) ---
    for x1, y1, x2, y2 in cracks:
        # black outer line (shadow glow)
        cv2.line(overlay, (x1, y1), (x2, y2), (0, 0, 0), 6)
        # strong red main line
        cv2.line(overlay, (x1, y1), (x2, y2), (255, 30, 30), 3)

    # --- DAMP BOXES (CYAN with WHITE outline) ---
    for (x, y, w, h) in damp:
        # white outer rectangle
        cv2.rectangle(overlay, (x, y), (x + w, y + h), (255, 255, 255), 6)
        # cyan main rectangle
        cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 255, 255), 3)

    return overlay

def analyze_cv(img):
    h, w = img.shape[:2]

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    cracks = []
    lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength=50,maxLineGap=10)
    if lines is not None:
        for l in lines:
            x1,y1,x2,y2 = l[0]
            cracks.append((x1,y1,x2,y2))

    damp = []
    blur = cv2.GaussianBlur(gray, (15,15), 0)
    _, thresh = cv2.threshold(blur, 0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        x,y,wc,hc = cv2.boundingRect(c)
        if wc*hc > 3000:
            damp.append((x,y,wc,hc))

    defects=[]
    summary_parts=[]
    recs=[]

    if cracks:
        defects.append({
            "type": "Crack",
            "severity": "Moderate",
            "confidence": 0.75,
            "notes": "Detected multiple crack-like line segments"
        })
        summary_parts.append("Crack indications present.")
        recs.append("Consider structural inspection.")

    if damp:
        defects.append({
            "type": "Damp",
            "severity": "Moderate",
            "confidence": 0.70,
            "notes": "Detected dark moisture-like patches"
        })
        summary_parts.append("Possible damp areas detected.")
        recs.append("Check ventilation or water ingress.")

    if not defects:
        defects.append({
            "type": "Unknown",
            "severity": "Low",
            "confidence": 0.20,
            "notes": "No significant issues"
        })
        summary_parts.append("No major visual defects found.")

    summary=" ".join(summary_parts)
    overlay = draw_overlays(img, cracks, damp)

    return defects, summary, recs, overlay