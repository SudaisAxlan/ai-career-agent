from langgraph.graph import StateGraph, START, END

from src.agents.state import StateAgent

from src.agents.nodes.user_node import user_node
from src.agents.nodes.profile_node import profile_node
from src.agents.nodes.search_planning import search_planning_node
from src.agents.nodes.search_node import search_node
from src.agents.nodes.match_node import match_node
from src.agents.nodes.response_node import response_node


graph = StateGraph(StateAgent)


graph.add_node("user_node", user_node)

graph.add_node("profile_node", profile_node)

graph.add_node(
    "search_planning_node",
    search_planning_node
)

graph.add_node(
    "search_node",
    search_node
)

graph.add_node(
    "match_node",
    match_node
)

graph.add_node(
    "response_node",
    response_node
)


graph.add_edge(
    START,
    "user_node"
)

graph.add_edge(
    "user_node",
    "profile_node"
)

graph.add_edge(
    "profile_node",
    "search_planning_node"
)

graph.add_edge(
    "search_planning_node",
    "search_node"
)

graph.add_edge(
    "search_node",
    "match_node"
)

graph.add_edge(
    "match_node",
    "response_node"
)

graph.add_edge(
    "response_node",
    END
)


agent = graph.compile()