from components.model import Model
from components.prompts import sql_prompt
from components.tools import sql_tools
from langgraph.prebuilt import create_react_agent

class SQLAgent:
    
    def __init__(self):
        self._model_obj = Model()
        self._model = self._model_obj.get_model()
        self._prompt = sql_prompt
        self._tools = sql_tools
    
    def get_agent(self):
        sql_agent = create_react_agent(
            model = self._model,
            tools = self._tools,
            prompt = self._prompt,
            name = "sql_agent"
        )
        return sql_agent