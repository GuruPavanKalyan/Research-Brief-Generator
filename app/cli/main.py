import argparse
from app.state import GraphState
from app.graph.workflow import build_graph

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, required=True)
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--user_id", type=str, default="user_abc")
    args = parser.parse_args()

    graph = build_graph()
    input_state = GraphState(
        topic=args.topic,
        depth=args.depth,
        follow_up=False,
        user_id=args.user_id
    )

    result = graph.invoke(input_state)

    planning_steps = result["planning_steps"]

    bullet_points = [step for step in planning_steps if step.strip().startswith("+")]

    print("Extracted Sub-questions:")
    for i, point in enumerate(bullet_points, 1):
        print(f"{i}. {point.strip('+ ').strip()}")

if __name__ == "__main__":
    main()
