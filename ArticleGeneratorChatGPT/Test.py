import os
import requests
from dotenv import load_dotenv

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
API_KEY = os.getenv("OPENAI_API_KEY")

# Endpoint URL
url = 'https://api.openai.com/v1/completions'

# Request headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

# Request payload
data = {
    'model': 'gpt-3.5-turbo-instruct',
    'prompt': 'Once upon a time',
    'max_tokens': 50
}

# Send POST request
response = requests.post(url, json=data, headers=headers)

# Print response
print(response.json())
