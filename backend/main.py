from dotenv import load_dotenv
import os

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils.similarity import semantic_similarity
from utils.changelog import generate_changelog
from backend.utils.llm_classifier import improve_text
from backend.utils.similarity import semantic_similarity
from backend.utils.changelog import generate_changelog
load_dotenv()

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str


@app.post("/enhance")
def enhance_text(request: TextRequest):

    revised_text = improve_text(request.text)

    similarity = semantic_similarity(request.text, revised_text)

    changes = generate_changelog(request.text, revised_text)

    return {
        "original": request.text,
        "revised": revised_text,
        "similarity": similarity,
        "changes": changes
    }