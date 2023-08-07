import openai
import os

from IPython.display import display, HTML
from dotenv import load_dotenv, find_dotenv
from prompt_examples import prompts

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

pre_prompt = "Check grammar and correct mistakes in following text: \n"


def get_prompt():
    key = input("Please provide a key for test prompt: ")
    if test_prompt := prompts.get(key):
        additional_info = input("Do you want to provide any additional info? ")
        value = f"{pre_prompt}{additional_info} \n\n {test_prompt}"
        return value


# use prompt for each object through iterable
def get_multi_prompt(seq):
    if isinstance(seq, dict):
        iterable_item = ' '.join(f'{k}: {v} \n' for k, v in seq.items())
    else:
        iterable_item = ' '.join(f'{num + 1}: {val}' for num, val in enumerate(seq))
    additional_info = input("Do you want to provide any additional info? ")
    return f"{pre_prompt} {additional_info} \n\n {iterable_item}"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# regular prompt
response = get_completion(get_prompt())
# iterable prompt
# response = get_completion(get_multi_prompt(seq=prompts.get("Espanol")))

print(response)
