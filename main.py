import openai
import os

from IPython.display import display, HTML
from dotenv import load_dotenv, find_dotenv
from prompt_examples import prompts

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')
KEY = "bookshelf"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


response = get_completion(prompts.get(KEY))
print(response)
