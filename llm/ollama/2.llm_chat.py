from langchain_ollama import ChatOllama
 
llm = ChatOllama(model="llama3.2:latest")
response = llm.invoke("Which is the capital of Australia and how many timezones we have there?")
print(response.content)
 
