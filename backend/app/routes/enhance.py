from fastapi import APIRouter, HTTPException
from app.services.rewrite_service import rewrite_text
from app.services.similarity_service import (
    compute_similarity,
    sentence_level_similarity
)
from app.services.validation_service import validate_similarity
from app.services.diff_service import generate_diff
from app.models.schemas import EnhanceResponse
from typing import Dict

router = APIRouter()

PARAGRAPH_THRESHOLD = 0.90
SENTENCE_THRESHOLD = 0.85
CRITICAL_THRESHOLD = 0.85


@router.post("/enhance", response_model=EnhanceResponse)
def enhance_text(request: Dict):

    if "text" not in request or not request["text"].strip():
        raise HTTPException(status_code=400, detail="Text input is required.")

    original_text = request["text"].strip()

    try:
        # ----------------------------
        # 1️⃣ First Rewrite Attempt
        # ----------------------------
        enhanced_text = rewrite_text(original_text)
        paragraph_similarity = compute_similarity(original_text, enhanced_text)

        # ----------------------------
        # 2️⃣ Retry If Below Threshold
        # ----------------------------
        if paragraph_similarity < PARAGRAPH_THRESHOLD:
            enhanced_text = rewrite_text(original_text, stricter=True)
            paragraph_similarity = compute_similarity(original_text, enhanced_text)

        # ----------------------------
        # 3️⃣ Sentence-Level Similarity
        # ----------------------------
        sentence_similarity = sentence_level_similarity(original_text, enhanced_text)

        # ----------------------------
        # 4️⃣ Safety Warning System
        # ----------------------------
        warning = None

        if paragraph_similarity < CRITICAL_THRESHOLD:
            warning = "⚠ Potential paragraph-level meaning drift detected."

        if sentence_similarity < SENTENCE_THRESHOLD:
            warning = "⚠ Sentence-level semantic drift detected. Review carefully."

        # ----------------------------
        # 5️⃣ Generate Change Log
        # ----------------------------
        changes = generate_diff(original_text, enhanced_text)

        # ----------------------------
        # 6️⃣ Final Response
        # ----------------------------
        return EnhanceResponse(
            original_text=original_text,
            enhanced_text=enhanced_text,
            similarity_score=round(paragraph_similarity, 4),
            changes=changes,
            warning=warning
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))