from pydantic import BaseModel
from typing import List, Optional


class ChangeItem(BaseModel):
    original: str
    enhanced: str
    change_type: str
    reason: str


class EnhanceResponse(BaseModel):
    original_text: str
    enhanced_text: str
    similarity_score: float
    changes: List[ChangeItem]
    warning: Optional[str] = None