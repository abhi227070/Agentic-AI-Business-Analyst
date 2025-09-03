from components.model import Model
from components.prompts import supervised_agent_prompt
from langgraph_supervisor import create_supervisor
from langgraph.checkpoint.memory import InMemorySaver
from agents.math_agent import MathAgent
from agents.sql_agent import SQLAgent
from agents.web_search_agent import WebSearchAgent

class SuperviserAgent:
    
    def __init__(self):
        math_agent_obj = MathAgent()
        self._math_agent = math_agent_obj.get_agent()
        
        web_search_agent_obj = WebSearchAgent()
        self._web_search_agent = web_search_agent_obj.get_agent()
        
        sql_agent_obj = SQLAgent()
        self._sql_agent = sql_agent_obj.get_agent()
        
        model_obj = Model()
        self._model = model_obj.get_model()
        self._prompt = supervised_agent_prompt
        
        self._checkpointer = InMemorySaver()
    
    def get_agent(self):
        
        superviser_agent = create_supervisor(
            model = self._model,
            agents = [self._math_agent, self._web_search_agent, self._sql_agent],
            prompt = self._prompt,
            add_handoff_back_messages=True,
            output_mode="full_history",
        ).compile(checkpointer = self._checkpointer)
        
        return superviser_agent