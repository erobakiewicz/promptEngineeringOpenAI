import openai
import os

from IPython.display import display, HTML
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


prompt = f"""
I want to build bookshelf for my room. The room is 3 meters wide and 4 meters long. I want it to be able to hold
5000 books. What are possible designs for the bookshelf? What materials should I use? What tools do I need? How much
does it cost in Poland (prices in PLN). 
Create a list of 5 possible and different from each other designs in length and width of shelf and in arrangement e.g.
in the corner, across the whole room. Create short summary of the each design (less than 100 words) with pros and cons.

"""
response = get_completion(prompt)
print(response)
# display(HTML(response))
