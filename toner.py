from typing import TypedDict 
## 1.dotenv stores the API key, variables in .env file 
from dotenv import load_dotenv # load_dotenv : load the variables from .env file
# 2.creating llm
from langchain.chat_models import init_chat_model 
# 3.Prompt Template
from langchain_core.prompts import ChatPromptTemplate
## 4.defining langgraph
from langgraph.graph import START, END, StateGraph
import os 

class EmailState(TypedDict): #3
    draft: str
    tone: str
    mail: str

load_dotenv() ## 1.calling a load_dotenv function from dotenv package
model_name=os.getenv('MODEL_NAME') # 1,retriving the value/variable ('MODEL_NAME') from .env file
model_provider=os.getenv('MODEL_PROVIDER') # 1. ||
llm = init_chat_model(model = model_name, model_provider = model_provider) # 2

# 4. def of function 
def change_email_tone(state:EmailState) -> EmailState:
    draft = state['draft'] 
    tone = state['tone']
    prompt= ChatPromptTemplate([   
        ("system", "you are expert email writer"),
        ("user", "consider the following draft email {draft} without changing facts and preserving the meaning"),
        ("user", "rewrite the email in less than 150 words in the following tone {tone}")
    ])
# creating a chain
    chain = prompt | llm
    response = chain.invoke({'draft': draft, 'tone': tone})
    state['mail'] = response.content
    return state

# defining graph 
toner_graph = StateGraph(EmailState) # 4
# adding nodes and edges
toner_graph.add_node("toner", change_email_tone)
toner_graph.add_edge(START, "toner")
toner_graph.add_edge("toner", END)


 # compile graph

graph= toner_graph.compile()