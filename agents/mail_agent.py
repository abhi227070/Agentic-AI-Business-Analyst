from components.tools import gmail_tools
from components.model import Model
from components.prompts import mail_prompt
from langgraph.prebuilt import create_react_agent

class MailAgent:
    
    def __init__(self):
        self._model_obj = Model()
        self._model = self._model_obj.get_model()
        self._prompt = mail_prompt
        self._tools = gmail_tools
        
    def get_agent(self):
        mail_agent = create_react_agent(
            model = self._model,
            tools= self._tools,
            prompt= (self._prompt),
            name= "mail_agent"
        )
        return mail_agent