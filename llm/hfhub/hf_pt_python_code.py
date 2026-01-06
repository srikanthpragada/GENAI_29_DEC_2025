from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate
import keys

model_id = "google/gemma-3-27b-it"   
client = InferenceClient(model=model_id, 
                         token= keys.HUGGINGFACE_KEY)

template_str = """Write a {language} function for the following requirement:
{task}
"""
prompt_template = PromptTemplate.from_template(template=template_str)

prompt = prompt_template.format(language = 'Python',
       task="Check whether a number is perfect number or not")

#print(prompt)


messages = [{"role": "user", "content": prompt}]

response = client.chat_completion(messages)
reply = response.choices[0].message.content
print(reply)
