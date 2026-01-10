import os
from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
)

messages = [
  {
    'role': 'user',
    'content': 'Which is the capital of Australia?',
  },
]

response = client.chat('gpt-oss:120b', messages=messages)
print(response.message.content)