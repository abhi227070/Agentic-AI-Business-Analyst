from langchain_core.tools import tool
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from components.model import Model
from components.prompts import math_prompt
from components.tools import math_tool

class MathAgent:
    
    def __init__(self):
        load_dotenv()
        self._model_obj = Model()
        self._model = self._model_obj.get_model()
        self._prompt = math_prompt
        self._tools = math_tool
    
    def get_agent(self):
        math_agent = create_react_agent(
            model = self._model,
            tools= [self._tools],
            prompt= (self._prompt),
            name= "math_agent"
        )
        return math_agent