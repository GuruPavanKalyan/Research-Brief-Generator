from app.state import GraphState
from app.graph.workflow import build_graph

if __name__ == "__main__":
    graph = build_graph()

    input_state = GraphState(
        topic="Applications of AI in Agriculture",
        depth=2,
        follow_up=False,
        user_id="user_abc"
    )

    result = graph.invoke(input_state)
    print("Available keys in result:", result.keys())

    planning_steps = result["planning_steps"]
    print(planning_steps)

    bullet_points = [step for step in planning_steps if step.strip().startswith("+")]

    print("Extracted Sub-questions:")
    for i, point in enumerate(bullet_points, 1):
        print(f"{i}. {point.strip('+ ').strip()}")
