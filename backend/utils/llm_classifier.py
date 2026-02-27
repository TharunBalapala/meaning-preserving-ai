# # from google import genai
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv


# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# def improve_text(text):

#     system_prompt = """You are a helpful assistant.
# Improve grammar, spelling and clarity.
# Preserve meaning exactly.
# Output only corrected text."""

#     response = client.models.generate_content(
#         model="gemini-1.5-flash",
#         config=types.GenerateContentConfig(
#             system_instruction=system_prompt,
#             temperature=0.3,
#             max_output_tokens=2000
#         ),
#         contents=text
#     )

#     return response.text.strip()
from transformers import pipeline

# Load local Hugging Face model
generator = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-medium"
)

def improve_text(text: str):
    prompt = f"""
    You are a Meaning-Preserving AI Writing Assistant.

    STRICT RULES:
    - Do NOT add new ideas.
    - Do NOT remove factual claims.
    - Do NOT expand the content.
    - Only improve grammar, spelling, clarity, and sentence structure.
    - Preserve EXACT meaning.

    Return ONLY the improved version.

    Original:
    {text}
    """

    response = generator(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )

    return response[0]["generated_text"]