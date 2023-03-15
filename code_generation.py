import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def create_code(prompt):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f"""
            Python Language
            {prompt}
        """,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0]["text"]


while True:
    prompt = input("Prompt: ")

    if "exit" in prompt or "quit" in prompt:
        break

    print(create_code(prompt))

print("Bye!!")
