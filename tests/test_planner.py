from app.graph.nodes.planner_node import planner_node  # Adjust the import if needed
from app.state import GraphState

def test_planner_node_basic():
    state = GraphState(topic="AI in Education", depth=2, user_id="test_user")
    result = planner_node.invoke(state)
    assert isinstance(result, GraphState)
    assert result.planning_steps
    assert any("+" in step for step in result.planning_steps)
