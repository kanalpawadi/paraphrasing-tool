from groq import Groq
import os
from dotenv import load_dotenv
import streamlit as st

# Load .env file for local development
load_dotenv()

# Get API key (Streamlit Cloud OR local .env)
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)


def generate_paraphrase(sentence, mode):

    prompt = f"""
You are an AI writing assistant.

Rewrite the sentence based on the selected mode.

Modes:
Standard → clear and natural rewrite
Fluency → improve grammar and readability
Formal → academic and professional tone
Creative → expressive and engaging rewrite

Mode: {mode}

Sentence:
{sentence}

Generate 3 different paraphrased versions.
Return them as a numbered list.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful AI paraphrasing assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content