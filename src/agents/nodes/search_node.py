

from src.agents.state import StateAgent
from src.tools.search_tool import search_tool


def search_node(state: StateAgent):

    search_plan = state.get("search_plan", "")

    queries = [
        query.strip()
        for query in search_plan.splitlines()
        if query.strip()
    ]

    all_results = []

    for query in queries[:5]:

        print(f"\nSearching: {query}")

        try:

            result = search_tool.invoke(query)

            if isinstance(result, dict):

                results = result.get("results", [])

                for item in results:

                    all_results.append({
                        "query": query,
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "content": item.get("content", ""),
                        "score": item.get("score", None)
                    })

            else:

                all_results.append({
                    "query": query,
                    "title": "",
                    "url": "",
                    "content": str(result),
                    "score": None
                })

        except Exception as e:

            print(f"Search failed for '{query}': {e}")

    return {
        "search_results": all_results
    }
