from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate
import keys

model_id = "openai/gpt-oss-120b"   
client = InferenceClient(model=model_id, 
                         token= keys.HUGGINGFACE_KEY)

language = "python"
task = "Check whether a number is perfect number or not"

# Using prompt template
template_str = """Write a {language} function for the following requirement:
{task}
"""
prompt_template = PromptTemplate.from_template(template=template_str)
prompt = prompt_template.format(language = language,
       task=task)

# using f string 
prompt = f"Write a {language} function for the following requirement: {task}"

messages = [{"role": "user", "content": prompt}]

response = client.chat_completion(messages)
reply = response.choices[0].message.content
print(reply)
