from pydantic import BaseModel
from typing import List

class Defect(BaseModel):
    type: str
    severity: str
    confidence: float
    notes: str

class InspectionResult(BaseModel):
    defects: List[Defect]
    summary: str
    recommendations: List[str]
    original_image: str | None = None
    overlay_image: str | None = None