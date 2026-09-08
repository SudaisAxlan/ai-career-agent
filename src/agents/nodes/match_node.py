import json

from src.agents.state import StateAgent
from src.llm.llm import local_llm


llm = local_llm()


def match_node(state: StateAgent):

    user_question = state.get("user_question", "")
    user_profile = state.get("user_profile", "")
    search_results = state.get("search_results", [])

    jobs = []

    for job in search_results[:10]:
        jobs.append({
            "title": job.get("title", ""),
            "url": job.get("url", ""),
            "content": job.get("content", "")[:1000]
        })

    prompt = f"""
Find the best 5 jobs for this candidate.

Job request:
{user_question}

Candidate:
{user_profile[:4000]}

Jobs:
{json.dumps(jobs)}

Return ONLY valid JSON like this:

[
  {{
    "job_title": "Machine Learning Intern",
    "company": "ABC",
    "location": "Karachi",
    "job_type": "Internship",
    "description": "Job description",
    "required_skills": "Python, ML",
    "experience": "0-1 years",
    "salary": "Not available",
    "posted_date": "Not available",
    "deadline": "Not available",
    "match_score": 90,
    "why_match": "Good Python and ML match",
    "apply_url": "EXACT URL FROM JOB",
    "source": "Indeed"
  }}
]

Rules:
- Maximum 5 jobs.
- Never invent a job.
- Never invent a company.
- Never invent a URL.
- Copy the URL exactly from the job data.
"""

    response = llm.invoke(prompt)

    text = response.content.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        matched_jobs = json.loads(text)
    except json.JSONDecodeError:
        print("Invalid JSON from LLM")
        print(text)
        matched_jobs = []

    return {
        "matched_jobs": matched_jobs
    }
