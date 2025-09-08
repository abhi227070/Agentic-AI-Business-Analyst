from components.tools import viz_tool
from components.model import Model
from components.prompts import visualization_prompt
from langgraph.prebuilt import create_react_agent

class VisualizationAgent:
    
    def __init__(self):
        model_obj = Model()
        self.model = model_obj.get_model()
        self.tools = [viz_tool]
        self.prompt = visualization_prompt
        
    def get_agent(self):
        
        visualization_agent = create_react_agent(
            model = self.model,
            tools = self.tools,
            prompt = self.prompt,
            name = "visualization_agent"
        )
        
        return visualization_agent