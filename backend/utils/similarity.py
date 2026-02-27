import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(text1, text2):

    embeddings = model.encode([text1, text2])

    emb1 = embeddings[0].reshape(1, -1)
    emb2 = embeddings[1].reshape(1, -1)

    score = cosine_similarity(emb1, emb2)[0][0]

    return round(float(score) * 100, 2)