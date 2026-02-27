# 🧠 Meaning Preserving AI Writing Assistant
## 🎯 Problem Statement

Build a web-based AI writing assistant that:

Improves grammar and clarity

Strictly preserves original meaning

Does not add or remove ideas

Computes a semantic similarity score

Displays a transparent change log

Shows side-by-side comparison

The system must enhance writing quality while guaranteeing semantic integrity.

## 🚀 Our Approach

Instead of blindly rewriting text, we built a controlled AI validation pipeline that verifies meaning preservation before delivering output.

### 🔄 Processing Flow

```
User Input
   ↓
Controlled Rewrite Prompt
   ↓
Diff Engine
   ↓
Semantic Similarity Check
   ↓
Validation Gate
   ↓
Final Output + Score + Change Log
```


## 🔐 Meaning Preservation Strategy
### 1️⃣ Controlled Rewriting

The model is strictly instructed to:

Improve grammar and fluency only

Avoid adding new information

Avoid removing intent

Preserve factual meaning

### 2️⃣ Semantic Similarity Validation

We compute embedding-based cosine similarity between:

Original text

Enhanced text

Then apply a validation threshold:

### Similarity Score	Action
```
≥ 0.92	✅ Accept
0.85 – 0.92	⚠ Flag
< 0.85	❌ Reject & Retry
```
This ensures no semantic drift.

### 3️⃣ Transparent Change Log

Word-level differences detected

Changes categorized (Grammar, Clarity, Structure)

Full side-by-side comparison

## 🏆 Core Principle

The system does not trust the rewrite blindly.
Every output must pass semantic validation before being accepted.
