from serpapi import GoogleSearch
from app.state import GraphState
import os


def search_node(state: GraphState) -> GraphState:
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise ValueError("Missing SERPAPI_API_KEY environment variable")

    results = []
    for step in state.planning_steps:
        search = GoogleSearch({
            "q": step,
            "api_key": api_key,
            "num": 3
        })
        res = search.get_dict()

        step_sources = []
        for r in res.get("organic_results", [])[:3]:
            step_sources.append(r.get("link", ""))
        results.extend(step_sources)

    state.sources = list(set(results))  
    print("Planning Steps:",state,"Planning Steps:END")
    return state
