from pipeline.supervised_agent import SuperviserAgent
from langchain_core.messages import HumanMessage
import warnings
<<<<<<< HEAD
import streamlit as st

warnings.filterwarnings('ignore')

# Initialize agent
=======

warnings.filterwarnings('ignore')

>>>>>>> 5687d1458f8f749b4f7c4e92d71858a83a35d320
agent_obj = SuperviserAgent()
agent = agent_obj.get_agent()

thread_id = '1'
config = {'configurable': {'thread_id': thread_id}}

<<<<<<< HEAD
# Initialize chat history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display old messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Chat input
user_input = st.chat_input("Type here...")

if user_input:
    # Save & display user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response with spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            placeholder = st.empty()
            full_response = ""

            final_message = None
            for message_chunk, metadata in agent.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=config,
                stream_mode="messages"
            ):
                if message_chunk.content:
                    final_message = message_chunk  # overwrite, keep last

            if final_message:
                full_response = final_message.content
                placeholder.markdown(full_response)

    # 👉 Only save to history (don’t re-display here)
    st.session_state['message_history'].append(
        {'role': 'assistant', 'content': full_response}
    )
=======
while True:
    
    user_input = input("User: ")
    
    if user_input.lower() in ("bye", "exit", "quit"):
        break
    
    response = agent.invoke({'messages': [HumanMessage(content= user_input)]}, config= config)
    
    print(f"AI: {response['messages'][-1].content}")
>>>>>>> 5687d1458f8f749b4f7c4e92d71858a83a35d320
