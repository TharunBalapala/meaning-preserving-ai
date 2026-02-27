from typing import Optional

class EnhanceResponse(BaseModel):
    original_text: str
    enhanced_text: str
    similarity_score: float
    changes: List[ChangeItem]
    warning: Optional[str] = None