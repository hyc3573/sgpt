import openai
import os
import langchain

os.environ["OPENAI_API_KEY"] = ""

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_input(input):
    input = input
    #입력이 어떻게 들어오는 지 몰라서 대충 씀 

def UseSgpt(input):
    response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    max_tokens = 1000,
    temperature=0.5,
    messages=[
        {"role":"system","content":"정확한 정보를 제공하는 도우미"},
        {"role":"user","content":f"{input}"},
        ]
    )
    res = response.choices[0].message.content

    return res