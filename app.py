# app.py

import streamlit as st
from langchain_core.messages import HumanMessage
from agent.langgraph_agent import build_langgraph

st.set_page_config(page_title="Medication Reminder AI", layout="centered")

st.title("💊 Medication Reminder AI Agent")

# Chat history state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Text input for user
user_input = st.text_input("👤 You:", key="user_input")

if st.button("Send") and user_input.strip() != "":
    st.session_state.messages.append(HumanMessage(content=user_input))

    # LangGraph agent
    agent = build_langgraph()
    state = {"messages": st.session_state.messages}
    updated_state = agent.invoke(state)

    st.session_state.messages = updated_state["messages"]

# Display conversation
st.write("### 💬 Conversation")
for msg in st.session_state.messages:
    role = "🧠 AI" if msg.type == "ai" else "👤 You"
    st.write(f"**{role}:** {msg.content}")
