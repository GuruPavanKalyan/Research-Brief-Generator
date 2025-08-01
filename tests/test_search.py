from app.graph.nodes.search_node import search_node
from app.state import GraphState

def test_search_node_outputs_sources():
    state = GraphState(topic="AI Ethics", depth=1, user_id="test_user", planning_steps=["+ Overview", "+ Case Studies"])
    result = search_node.invoke(state)
    assert isinstance(result.sources, list)
    assert all("http" in url for url in result.sources)
