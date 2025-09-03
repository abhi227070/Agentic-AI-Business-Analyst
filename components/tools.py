from langchain_core.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from components.model import Model

#-------------------------------------------------------------------------
# Math tool
#-------------------------------------------------------------------------

@tool
def math_tool(expression: str) -> float:
    """
    A tool to evaluate mathematical expressions.

    Args:
        expression (str): A valid mathematical expression as a string.
                        Example: "5+10*2" or "(12/4)+3".

    Returns:
        float: The computed result of the expression.

    Raises:
        ValueError: If the expression is invalid or unsafe.
    """
    try:
        # Create a safe evaluation environment
        allowed_names = {
            k: v for k, v in vars(__import__("math")).items() if not k.startswith("__")
        }
        allowed_names["abs"] = abs
        allowed_names["round"] = round

        # Evaluate safely
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return float(result)
    except Exception as e:
        raise ValueError(f"Invalid expression: {expression}. Error: {str(e)}")
    
#-------------------------------------------------------------------------
# Web Search tool
#-------------------------------------------------------------------------

load_dotenv()
search = SerpAPIWrapper()

@tool
def web_search_tool(query: str) -> str:
    """
    Use this tool to look up recent, factual, or real-time information on the web.
    Also you can use this tool to get current datetime, weather or other realtime information. 
    Always call this tool if the user asks for news, current events, statistics, 
    product details, or anything that requires searching online.
    
    Input: A search query string.
    Output: A brief summary of the top relevant search results.
    """
    return search.run(query)

#-------------------------------------------------------------------------
# SQL tool
#-------------------------------------------------------------------------

db = SQLDatabase.from_uri("mysql+mysqlconnector://root:abhijeet123@localhost:3306/youtube")
model_obj = Model()
model = model_obj.get_model()
toolkit = SQLDatabaseToolkit(db = db, llm=model)
sql_tools = toolkit.get_tools()