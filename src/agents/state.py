from typing import TypedDict


class CareerAgentState(TypedDict, total=False):
    user_question: str
    user_profile: str
    search_plan: str
    search_results: str
    matched_jobs: str
    response: str