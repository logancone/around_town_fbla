from dotenv import load_dotenv
from openai import OpenAI
import os
import time

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

start = time.time()
response = client.responses.create(
    model="gpt-5-nano",
    input='hello',
    reasoning={
        "effort": "low"
    }
)

print(response.output_text)
print(time.time() - start)

start = time.time()
response = client.responses.create(
    model='gpt-5-nano',
    input="what is your name?",
    reasoning={
        "effort": "low"
    }
)

print(response.output_text)
print(time.time() - start)

start = time.time()
response = client.responses.create(
    model='gpt-5-nano',
    input="who made you?",
    reasoning={
        "effort": "low"
    }
)
print (response.output_text)
print(time.time() - start)