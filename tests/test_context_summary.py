from app.graph.nodes.context_summarize import context_summary_node
from app.state import GraphState

def test_context_summary_generates_summary():
    state = GraphState(topic="AI Policy", depth=2, user_id="test_user", planning_steps=["+ Intro", "+ Future Impact"])
    result = context_summary_node.invoke(state)
    assert result.context_summary
    assert isinstance(result.context_summary, str)
    assert len(result.context_summary) > 10
