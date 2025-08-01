from app.graph.nodes.synthesis_node import synthesizer_node
from app.state import GraphState, Summary

def test_synthesizer_node_combines_summaries():
    summaries = [
        Summary(source_url="https://example.com", content="AI is evolving", summary="AI progress."),
        Summary(source_url="https://another.com", content="AI in healthcare", summary="AI in health."),
    ]
    state = GraphState(topic="AI", depth=2, user_id="u123", summaries=summaries)
    result = synthesizer_node.invoke(state)
    assert result.final_brief is not None
    assert len(result.final_brief.summary) > 0
