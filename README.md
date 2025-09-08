# Agentic-AI-Business-Analyst

Agentic AI Business Analyst is an LLM-powered multi-agent assistant built with [LangGraph](https://github.com/langchain-ai/langgraph) that automates business analytics, visualization, and reporting. It leverages multiple specialized agents (math, SQL, web search, visualization, and email) to answer business questions, generate insights, create charts, and send reports.

---

## Features

- **Multi-Agent Orchestration:** Supervisor agent delegates tasks to specialized agents for math, SQL, web search, visualization, and email.
- **Natural Language Interface:** Ask business questions in plain English.
- **Automated Data Analysis:** Query SQL databases, perform calculations, and summarize results.
- **Data Visualization:** Generate charts (bar, pie, line, histogram) using matplotlib/seaborn.
- **Web Search Integration:** Fetch real-time information and news.
- **Email Automation:** Compose and send emails with generated reports or insights.
- **Streamlit UI & Notebook Support:** Interact via web UI or Jupyter notebook.

---

## Project Structure

```
.
├── app.py                      # Streamlit web app entry point
├── requirements.txt            # Python dependencies
├── agents/                     # Agent implementations
├── components/                 # Tools, prompts, and model wrappers
├── pipeline/                   # Supervisor agent and orchestration logic
├── notebook/                   # Jupyter notebooks for development/testing
└── ...
```

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/Agentic-AI-Business-Analyst.git
cd Agentic-AI-Business-Analyst
```

### 2. Install Dependencies

It is recommended to use a virtual environment.

```sh
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys and configuration as needed (e.g., SerpAPI, Gmail credentials, database URI).

### 4. Configure Database

Update the database URI in `components/tools.py` to point to your MySQL database.

### 5. Run the Application

#### Streamlit Web App

```sh
streamlit run app.py
```

#### Jupyter Notebook

See `notebook/development1.ipynb` for interactive examples.

---

## Agents Overview

- **Math Agent:** Evaluates mathematical expressions and calculations.
- **SQL Agent:** Interacts with SQL databases to answer data-related queries.
- **Web Search Agent:** Fetches real-time information from the web.
- **Visualization Agent:** Generates charts and visualizations.
- **Mail Agent:** Composes and sends emails using Gmail API.

---

## Example Usage

- **Ask a business question:**  
  _"What was the total revenue last quarter?"_
- **Request a chart:**  
  _"Show me a bar chart of monthly sales for 2023."_
- **Send a report:**  
  _"Email the latest revenue report to the finance team."_

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [SerpAPI](https://serpapi.com/)
- [Google Gmail API](https://developers.google.com/gmail/api)

---

## Contact

For questions or support, please open an issue or contact the maintainer.
