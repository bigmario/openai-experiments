import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

messages = [
    {
        "role": "system",
        "content": "You’re a kind, helpful, articulate, creative, funny, clever, and very friendly",
    },
]


def create_generation(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=content,
        temperature=1,
        max_tokens=500,
        frequency_penalty=0,
        presence_penalty=0.6,
    )

    answer = response.choices[0].message.content
    print(answer)
    messages.append({"role": "assistant", "content": answer})


while True:
    user_input = input("You: ")

    if "exit" in user_input or "quit" in user_input:
        break

    messages.append({"role": "user", "content": user_input})

    create_generation(messages)

print("Bye!!")
