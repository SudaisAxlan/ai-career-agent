from src.agents.graph import agent
from src.agents.state import StateAgent


question: StateAgent = {
    "user_question": "I want a Machine Learning Internship in Lahore.",
    "user_profile": "",
    "search_plan": "",
    "search_results": "",
    "matched_jobs": "",
    "response": ""
}


result = agent.invoke(question)

print(result["response"])
