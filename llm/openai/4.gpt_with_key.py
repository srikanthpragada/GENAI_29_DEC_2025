
import keys 
from openai import OpenAI

client = OpenAI(api_key=keys.OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-4o-mini",
    input="What is the capital of Spain?"
)

print(response.output_text)

