# agent/langgraph_agent.py

from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
import os

# 🧠 Load Groq API key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

# 📄 Define state
class ReminderState(TypedDict):
    messages: Annotated[list, HumanMessage | AIMessage]

# 🤖 Use Groq model instead of OpenAI
def run_groq(state: ReminderState):
    model = ChatGroq(
        model="llama3-70b-8192",  # Or "llama3-70b-8192"
        temperature=0.3,
        api_key=groq_api_key
    )
    response = model.invoke(state["messages"])
    state["messages"].append(response)
    return state

# 🔁 Build LangGraph workflow
def build_langgraph():
    workflow = StateGraph(ReminderState)
    workflow.add_node("chat", RunnableLambda(run_groq))
    workflow.set_entry_point("chat")
    workflow.set_finish_point("chat")
    return workflow.compile()
