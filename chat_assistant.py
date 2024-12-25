from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

from models import UserIntent

chat_history = []

def get_intent(command):
    try:
        llm = ChatOllama(model="llama3.1:8b")
        llm_structured_output = llm.with_structured_output(UserIntent)
        print("Analyzing.....")
        response = llm_structured_output.invoke(command)
        return response
    except Exception as e:
        print(f"get_intent method failed. Exception: {e}")

def chat(query):
    try:
        llm = ChatOllama(model="llama3.1:8b")
        chat_template = ChatPromptTemplate.from_messages([
            ("system", "You are helpful chat assistant"),
            (MessagesPlaceholder(variable_name="history")),
            ("user", "{query}")
        ])

        chain = chat_template | llm
        print("Analyzing.....")
        response = chain.invoke({"history": chat_history, "query":query})
        chat_history.append(HumanMessage(content=query))
        chat_history.append(AIMessage(content=response.content))
        return response.content
    except Exception as e:
        print(f"chat method failed. Exception: {e}")