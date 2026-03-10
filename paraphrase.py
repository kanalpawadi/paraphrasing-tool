from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


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
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content