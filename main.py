import openai
import os

from IPython.display import display, HTML
from dotenv import load_dotenv, find_dotenv
from prompt_examples import prompts

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_prompt():
    key = input("Please provide a key for test prompt: ")
    if test_prompt := prompts.get(key):
        additional_info = input("Do you want to provide any additional info? ")
        value = f"{additional_info} \n\n {test_prompt}"
        return value


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


response = get_completion(get_prompt())
print(response)
