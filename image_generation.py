import os
import requests
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_image(prompt: str):
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    return image_url


while True:
    prompt = input("Input: ")

    if "exit" in prompt or "quit" in prompt:
        break

    answer = generate_image(prompt)
    image = requests.get(answer)
    with open("./results/image.jpg", "wb") as transcription_file:
        transcription_file.write(image.content)

    print("Image Created!!")

print("Bye!!")
