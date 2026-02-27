from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def compute_similarity(text1: str, text2: str) -> float:
    emb1 = embeddings_model.embed_query(text1)
    emb2 = embeddings_model.embed_query(text2)

    emb1 = np.array(emb1)
    emb2 = np.array(emb2)

    # ✅ NORMALIZATION ADDED HERE
    emb1 = emb1 / np.linalg.norm(emb1)
    emb2 = emb2 / np.linalg.norm(emb2)

    score = cosine_similarity([emb1], [emb2])[0][0]
    return float(score)

def sentence_level_similarity(original: str, enhanced: str) -> float:
    orig_sentences = [s.strip() for s in original.split(".") if s.strip()]
    enh_sentences = [s.strip() for s in enhanced.split(".") if s.strip()]

    min_length = min(len(orig_sentences), len(enh_sentences))
    if min_length == 0:
        return 0.0

    scores = []

    for i in range(min_length):
        emb1 = np.array(embeddings_model.embed_query(orig_sentences[i]))
        emb2 = np.array(embeddings_model.embed_query(enh_sentences[i]))

        emb1 = emb1 / np.linalg.norm(emb1)
        emb2 = emb2 / np.linalg.norm(emb2)

        score = cosine_similarity([emb1], [emb2])[0][0]
        scores.append(score)

    return float(sum(scores) / len(scores))