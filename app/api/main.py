import os
# from langchain_core.tracers import LangChainTracer
from langchain_core.tracers.context import tracing_v2_enabled
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from app.state import GraphState
from app.graph.workflow import build_graph
import os
from dotenv import load_dotenv




load_dotenv()


app = FastAPI()
graph = build_graph()


# Request and response models
class Summary(BaseModel):
    source_url: str
    content: str
    summary: str


class FinalBrief(BaseModel):
    topic: str
    depth: int
    user_id: str
    summary: str
    references: List[Summary]


class InputState(BaseModel):
    topic: str
    depth: int
    follow_up: bool
    user_id: str
    planning_steps: Optional[List[str]] = []
    sources: Optional[List[str]] = []
    summaries: Optional[List[Summary]] = []
    final_brief: Optional[FinalBrief] = None
    context_summary: Optional[str] = ""
    serpapi_key: str


# Helper function for creating points
def format_bullet_points(bullet_points: List[str]) -> List[str]:
    return [f"{i}. {point.strip('+• ').strip()}" for i, point in enumerate(bullet_points, 1)]


# FastAPI endpoint
@app.post("/generate-brief")
def generate_brief(state: InputState):
    graph_state = GraphState(**state.dict())
    project_name = "BriefGen-Tracing-Demo"
    os.environ["SERPAPI_API_KEY"] = state.serpapi_key
    with tracing_v2_enabled(project_name=project_name):
       result = graph.invoke(graph_state)
    
    planning_steps = result["planning_steps"]
    bullet_points = [step for step in planning_steps if step.strip().startswith("+")]
    # Format planning steps
    formatted_steps = format_bullet_points(bullet_points)
    print("Pavan------------------------------------Result")

    print(result)
    return {
        "topic": result["topic"],
        "depth": result["depth"],
        "user_id": result["user_id"],
        "context_summary":result["context_summary"],
        "planning_steps": formatted_steps,
        "raw_planning_steps": result["planning_steps"],
        "summaries": result["summaries"],
        "final_brief": result["final_brief"].summary
        
    }
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>BriefForge API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 80px;
                    background-color: #f9f9f9;
                }
                h1 {
                    color: #1e88e5;
                }
                p {
                    font-size: 18px;
                }
                .footer {
                    margin-top: 40px;
                    color: #888;
                }
            </style>
        </head>
        <body>
            <h1>BriefForgeGuru: Multi-AI Research Agent</h1>
            <p><strong>Generate structured research briefs using LLMs + Web Search</strong></p>
            <p>API Endpoint: <code>POST /generate-brief</code></p>
            <div class="footer">
                <p>Built by <strong>Guru Pavan Kalyan</strong></p>
                <p>Bring your own SerpAPI key when calling the API</p>
            </div>
        </body>
    </html>
    """
