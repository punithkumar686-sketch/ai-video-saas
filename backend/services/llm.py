import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_script(topic: str):
    prompt = f"""
    Create a viral 30-second YouTube Short script.
    Topic: {topic}
    Make it engaging, fast-paced, and attention grabbing.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
