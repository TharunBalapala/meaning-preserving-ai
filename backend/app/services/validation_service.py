SIMILARITY_THRESHOLD = 0.90

def validate_similarity(score: float) -> bool:
    return score >= SIMILARITY_THRESHOLD