import base64
import cv2
import numpy as np

def to_base64(img_np):
    _, buffer = cv2.imencode(".jpg", img_np)
    return base64.b64encode(buffer).decode("utf-8")