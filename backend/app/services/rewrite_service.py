from langchain_google_genai import ChatGoogleGenerativeAI
import os

STRICT_PROMPT = """
You are a professional academic editor.

Your task:
- Improve grammar, spelling, clarity and sentence structure.
- Preserve the exact original meaning.
- Do NOT add new information.
- Do NOT remove factual meaning.
- Do NOT expand the content.
- Do NOT introduce new examples.
- Do NOT change intent.

Return ONLY the improved text.
"""

STRICTER_PROMPT = """
You previously altered meaning.

Rewrite again strictly:
- Only fix grammar and clarity.
- Keep sentence structure close to original.
- Do NOT rephrase creatively.
- Do NOT expand content.
- Do NOT compress content.
- Maintain semantic equivalence strictly.

Return ONLY the corrected version.
"""

def rewrite_text(text: str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    prompt = f"""{STRICT_PROMPT}

Text:
{text}
"""

    response = llm.invoke(prompt)
    return response.content