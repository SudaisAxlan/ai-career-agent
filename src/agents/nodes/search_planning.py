
from src.agents.state import StateAgent
from src.llm.llm import local_llm



llm = local_llm()


def search_planning_node(state: StateAgent):

    user_question = state.get("user_question", "")
    user_profile = state.get("user_profile", "")

    prompt = f"""
You are a job search query generation agent.

USER REQUEST:
{user_question}

CANDIDATE PROFILE:
{user_profile}

Generate exactly 5 short search queries for finding REAL job
or internship opportunities.

Rules:

- Queries must be short.
- Each query must be less than 150 characters.
- Focus on job title, skills and location.
- Do not explain anything.
- Do not summarize the candidate.
- Return ONLY the queries.
- One query per line.

Example:

Machine Learning Internship Lahore
AI Internship Lahore Pakistan
Python Machine Learning Intern Lahore
Machine Learning Intern Pakistan
AI Engineer Internship Lahore
"""

    response = llm.invoke(prompt)

    search_plan = response.content.strip()

    return {
        "search_plan": search_plan
    }