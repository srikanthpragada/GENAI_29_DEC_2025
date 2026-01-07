# Set environment variable GOOGLE_API_KEY to Google key.

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

system_message = {"role" : "system" , "content" : "Give short answers"}
messages = [system_message]

while True:
    prompt = input("Enter prompt [q to quit, c to create new chat] :")
    if prompt.lower() == 'q':
        break 

    if prompt.lower() == 'c':
        messages = [system_message]
        continue 
        
    messages.append( {"role" : "user", "content" : prompt})  # HumanMessage
    response = model.invoke(messages)
    print(response.content)
    messages.append( {"role" : "assistant", "content" : response.content})  # AIMessage
