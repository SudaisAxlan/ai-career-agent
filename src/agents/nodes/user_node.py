
from src.agents.state import StateAgent


def user_node(state: StateAgent):

    user_question = state.get("user_question", "").strip()

    return {
        "user_question": user_question
    }