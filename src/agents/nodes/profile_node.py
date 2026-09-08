from src.agents.state import StateAgent
from src.llm.llm import local_llm


llm = local_llm()


def profile_node(state: StateAgent):

    user_question = state.get("user_question", "")

    # Resume text comes from user_profile
    resume_text = state.get("user_profile", "")

    prompt = f"""
You are a professional resume analysis agent.

Analyze the following resume and create a concise but complete
candidate profile.

Extract:

- Name
- Location
- Skills
- Programming languages
- Frameworks and libraries
- Education
- Work experience
- Internships
- Projects
- Certifications
- Relevant AI/ML experience
- Relevant software engineering experience
- Other important professional information

Do not invent information that is not present in the resume.

User's job/internship request:
{user_question}

Resume text:
{resume_text}

Return a clean candidate profile that can be used by another
AI agent for job searching and job matching.
"""

    response = llm.invoke(prompt)

    return {
        "user_profile": response.content
    }