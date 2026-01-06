from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
model = init_chat_model("gpt-4o-mini",
                        model_provider="openai",
                        temperature=0.7,
                        max_tokens=300)
response = model.invoke("Write a short story about Moon in 5 sentenses")
print(response.content)
