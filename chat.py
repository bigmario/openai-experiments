import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """The following is a conversation with an AI assistant. 
            The assistant is helpful, articulate, creative, funny, clever, and very friendly.
            Human: Hello, who are you?
            AI: I am an AI created by OpenAI. How can I help you today?
            Human:
         """

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def create_generation():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + start_sequence,
        temperature=1,
        max_tokens=500,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\nHuman:", "\n"],
    )

    answer = response.choices[0]["text"]
    new_prompt = prompt + start_sequence + answer + restart_sequence

    return answer, new_prompt


while True:
    prompt += input("You: ")

    if "exit" in prompt or "quit" in prompt:
        break

    answer, prompt = create_generation()
    print(answer)

print("Bye!!")
