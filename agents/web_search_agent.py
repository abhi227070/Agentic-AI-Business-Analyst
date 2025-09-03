from components.model import Model
from components.tools import web_search_tool
from components.prompts import web_search_prompt
from langgraph.prebuilt import create_react_agent

class WebSearchAgent:
    
    def __init__(self):
        self._model_obj = Model()
        self._model = self._model_obj.get_model()
        self._prompt = web_search_prompt
        self._tools = web_search_tool
        
    def get_agent(self):
        web_search_agent = create_react_agent(
            model = self._model,
            tools = [self._tools],
            prompt = self._prompt,
            name = 'web_search_agent'
        )
        return web_search_agent