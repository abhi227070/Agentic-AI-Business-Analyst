from components.model import Model
from components.prompts import supervised_agent_prompt
from langgraph_supervisor import create_supervisor
from langgraph.checkpoint.memory import InMemorySaver
from agents.math_agent import MathAgent
from agents.sql_agent import SQLAgent
from agents.web_search_agent import WebSearchAgent
<<<<<<< HEAD
from agents.vizualization_agent import VisualizationAgent
from agents.mail_agent import MailAgent
=======
>>>>>>> 5687d1458f8f749b4f7c4e92d71858a83a35d320

class SuperviserAgent:
    
    def __init__(self):
<<<<<<< HEAD
        
=======
>>>>>>> 5687d1458f8f749b4f7c4e92d71858a83a35d320
        math_agent_obj = MathAgent()
        self._math_agent = math_agent_obj.get_agent()
        
        web_search_agent_obj = WebSearchAgent()
        self._web_search_agent = web_search_agent_obj.get_agent()
        
        sql_agent_obj = SQLAgent()
        self._sql_agent = sql_agent_obj.get_agent()
        
<<<<<<< HEAD
        visualization_agent_obj = VisualizationAgent()
        self._visualization_agent = visualization_agent_obj.get_agent()
        
        mail_agent_obj = MailAgent()
        self._mail_agent = mail_agent_obj.get_agent()
        
        model_obj = Model()
        self._model = model_obj.get_model()
        self._prompt = supervised_agent_prompt
=======
        model_obj = Model()
        self._model = model_obj.get_model()
        self._prompt = supervised_agent_prompt
        
>>>>>>> 5687d1458f8f749b4f7c4e92d71858a83a35d320
        self._checkpointer = InMemorySaver()
    
    def get_agent(self):
        
        superviser_agent = create_supervisor(
            model = self._model,
<<<<<<< HEAD
            agents = [self._math_agent, self._web_search_agent, self._sql_agent, self._visualization_agent, self._mail_agent],
=======
            agents = [self._math_agent, self._web_search_agent, self._sql_agent],
>>>>>>> 5687d1458f8f749b4f7c4e92d71858a83a35d320
            prompt = self._prompt,
            add_handoff_back_messages=True,
            output_mode="full_history",
        ).compile(checkpointer = self._checkpointer)
        
        return superviser_agent