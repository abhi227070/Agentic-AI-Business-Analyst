from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA

load_dotenv()

model = ChatNVIDIA(model = "nvidia/nvidia-nemotron-nano-9b-v2")

class Model:
    
    def __init__(self):
        load_dotenv()
        
    def get_model(self):
        model = ChatNVIDIA(model = "nvidia/nvidia-nemotron-nano-9b-v2")
        return model