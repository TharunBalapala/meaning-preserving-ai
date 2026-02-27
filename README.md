# meaning-preserving-ai
AI writing assistant with semantic validation and meaning-preservation pipeline
# Meaning Preserving AI Writing Assistant

## Overview
This project is a semantic-safe AI writing assistant that improves grammar and clarity 
while strictly preserving original meaning.

## Core Features
- Controlled AI rewriting
- Embedding-based semantic similarity validation
- Cosine similarity scoring
- Transparent change log
- Validation threshold system
- Retry mechanism for semantic drift

## Architecture
User Input
   ↓
Preprocessing
   ↓
Controlled Rewrite Prompt
   ↓
Diff Engine
   ↓
Embedding Similarity Check
   ↓
Validation Gate
   ↓
Final Output + Logs + Score

## Tech Stack
- FastAPI
- SentenceTransformers
- OpenAI / LLM
- React (Frontend)
