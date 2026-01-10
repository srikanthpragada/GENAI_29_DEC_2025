from langchain.chat_models import init_chat_model
model = init_chat_model("gemini-2.5-flash",
                        model_provider="google_genai",
                        temperature=0.9,
                        max_output_tokens=300)
response = model.invoke("Write a short story about Moon in 5 sentenses")
print(response.content)
