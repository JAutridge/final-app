# Load environment variables from a .env file
from dotenv import load_dotenv
import os

# LangChain message types for conversation memory
from langchain_core.messages import HumanMessage, AIMessage

# Converts LLM output into a plain string
from langchain_core.output_parsers import StrOutputParser

# Used to build structured chat prompts
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Google Gemini LLM wrapper for LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st

# # Gradio for building the web chat UI
# import gradio as gr

# Load variables from .env into environment
load_dotenv()

# Read Gemini API key from environment
API = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",  # Fast Gemini chat model
    api_key=API,                    # Authentication
    temperature=0.5                 # Creativity level
)

# System prompt defines the assistant's personality
system = """
You are Lebron James.
"""

print("Ask any question to LB James.")

# Build the chat prompt template
# - system: personality / instructions
# - history: previous messages (memory)
# - human: current user input
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{human}")
    ]
)

# Build LangChain pipeline:
# prompt → Gemini model → string output
chain = prompt | llm | StrOutputParser()

# Chat function used by Gradio
def chat(human, hist):
    langchain_history = []

    # Convert Gradio chat history into LangChain message objects
    for mes in hist:
        if mes["role"] == "user":
            langchain_history.append(
                HumanMessage(content=mes["content"])
            )
        elif mes["role"] == "assistant":
            langchain_history.append(
                AIMessage(content=mes["content"])
            )

    # Call the LLM with current input and conversation history
    response = chain.invoke({
        "human": human,
        "history": langchain_history
    })

    # Return:
    # 1. Empty string → clears input box
    # 2. Updated chat history for Gradio
    return "", hist + [
        {"role": "user", "content": human},
        {"role": "assistant", "content": response}
    ]

st.title("LeBron Chat-Bot", text_alignment="center")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])




# User input
prompt = st.chat_input("Type your message here...")
print(1.,prompt)

message = chat(
    human=prompt,
    hist=st.session_state.messages
)

if prompt:
    icon = st.chat_message("ai",avatar="🏀")
    ai_answer = (message[1][1]['content'])
    print(ai_answer)
    st.write( f'You: {prompt}')
    st.write(f'LeBron: {ai_answer}')


# # Build the Gradio UI
# with gr.Blocks(
#     title="Chat with Lebron James",
#     theme=gr.themes.Soft()
# ) as page:
#
#     # App title and description
#     gr.Markdown(
#         """
#         # Chat with Lebron James
#         Chat with Lebron James The Great Champ
#         """
#     )
#
#     # Chat display component
#     chatbot = gr.Chatbot()
#
#     # Text input field for user messages
#     message = gr.Text(placeholder="Ask LeBron a question...")
#
#     # When user presses Enter, call chat()
#     message.submit(chat, [message, chatbot], [message, chatbot])
#
#     # Button to clear chat (not wired yet)
#     clear = gr.Button("Clear")
#
# # Launch the Gradio app
# page.launch(share=True)