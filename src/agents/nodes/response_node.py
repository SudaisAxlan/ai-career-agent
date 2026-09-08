from src.agents.state import StateAgent
from src.llm.llm import local_llm


llm = local_llm()


def response_node(state: StateAgent):

    user_question = state.get("user_question", "")
    matched_jobs = state.get("matched_jobs", "")

    prompt = f"""
You are a professional AI career assistant.

The user asked:

{user_question}

The job matching agent selected these jobs:

{matched_jobs}

Create the final answer.

Return ONLY the final job recommendations.

For every job include:

## Rank. Job Title

**Company:** 
**Location:** 
**Job Type:** 
**Posted Date:** 
**Match Score:** 

### Description
Give the available job description.

### Required Skills
List the important skills.

### Experience
Give the required experience.

### Salary
Give the salary if available.

### Deadline
Give the application deadline if available.

### Why This Matches
Explain briefly why the candidate matches this job.

### Apply
Give the exact application URL.

### Source
Give the source/platform.

IMPORTANT:

- Never invent information.
- Never invent URLs.
- Never modify URLs.
- Use exactly the URLs provided by the matching agent.
- If something is unavailable, say "Not available".
- Return maximum 5 jobs.
- Do not add generic career advice.
"""

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }