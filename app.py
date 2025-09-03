from pipeline.supervised_agent import SuperviserAgent
from langchain_core.messages import HumanMessage
import warnings

warnings.filterwarnings('ignore')

agent_obj = SuperviserAgent()
agent = agent_obj.get_agent()

thread_id = '1'
config = {'configurable': {'thread_id': thread_id}}

while True:
    
    user_input = input("User: ")
    
    if user_input.lower() in ("bye", "exit", "quit"):
        break
    
    response = agent.invoke({'messages': [HumanMessage(content= user_input)]}, config= config)
    
    print(f"AI: {response['messages'][-1].content}")