# import pytest
from app.graph.nodes.summarizer import summarizer_node
from app.state import GraphState


def test_summarizer_node():
    dummy_state = GraphState(
        sources=["https://example.com/test1"],
        fetched_contents=["This is a test article about AI trends and applications in 2025."]
    )

    updated_state = summarizer_node(dummy_state)

    assert updated_state.summaries is not None
    assert len(updated_state.summaries) == 1
    assert "AI" in updated_state.summaries[0].summary

def test_empty_content():
    dummy_state = GraphState(
        sources=["https://example.com/test2"],
        fetched_contents=[""]
    )

    updated_state = summarizer_node(dummy_state)
    assert "No content" in updated_state.summaries[0].summary or updated_state.summaries[0].summary == ""


