from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def improve_text(text):

    system_prompt = """You are a helpful assistant.
Improve grammar, spelling and clarity.
Preserve meaning exactly.
Output only corrected text."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3,
            max_output_tokens=2000
        ),
        contents=text
    )

    return response.text.strip()