from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.state import GraphState
from app.utils.llms import get_groq_llm
from app.graph.nodes.search_node import search_node
from app.graph.nodes.summarizer import summarizer_node
from app.graph.nodes.synthesis_node import synthesis_node
from app.graph.nodes.context_summarize import context_summarization_node



def planner_node(state: GraphState) -> GraphState:
    prompt = ChatPromptTemplate.from_template("""
    You are a research planner.

    Given the research topic: "{topic}" and the depth level: {depth}, break it down into {depth} sub-steps or specific sub-questions.

    Respond in bullet points.
    """)
    
    llm = get_groq_llm("llama3-70b-8192")  
    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"topic": state.topic, "depth": state.depth})
    steps = [step.strip("-• ").strip() for step in response.split("\n") if step.strip()]
    state.planning_steps = steps
    return state


def build_graph():
    builder = StateGraph(GraphState)
    builder.add_node("planner", planner_node)
    builder.add_node("search", search_node)
    builder.add_node("summarizer",summarizer_node)
    builder.add_node("synthesis",synthesis_node)
    builder.add_node("context_summary",context_summarization_node)


    # start -> planner -> END
    builder.set_entry_point("planner")
    builder.add_edge("planner","search")
    builder.add_edge("search","summarizer")
    builder.add_edge('summarizer',"synthesis")
    builder.add_edge("synthesis","context_summary")
    builder.add_edge("context_summary", END)

    return builder.compile()
