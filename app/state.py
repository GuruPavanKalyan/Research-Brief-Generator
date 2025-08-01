from pydantic import BaseModel
from typing import List, Optional

class SourceSummary(BaseModel):
    source_url: str
    content: str
    summary: str

class FinalBrief(BaseModel):
    topic: str
    depth: int
    user_id: str
    summary: str
    references: List[SourceSummary]

class GraphState(BaseModel):
    topic: str
    depth: int
    follow_up: bool
    user_id: str
    planning_steps: Optional[List[str]] = None
    sources: Optional[List[str]] = None
    summaries: Optional[List[SourceSummary]] = []
    final_brief: Optional[FinalBrief] = None
    context_summary: Optional[str] = None
