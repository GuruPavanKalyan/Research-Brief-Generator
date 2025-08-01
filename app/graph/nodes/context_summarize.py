from app.utils.llms import get_groq_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.state import GraphState

def context_summarization_node(state: GraphState) -> GraphState:
    if not state.follow_up or not state.final_brief:
        return state  

    llm = get_groq_llm("llama3-70b-8192")
    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant. The following is a previously generated brief from the user:

Topic: {topic}
Summary:
{summary}

Generate a compact context summary (3–4 lines) capturing the essence of the brief. Do not include bullet points or headings.
""")
    
    chain = prompt | llm | StrOutputParser()
    
    context_summary = chain.invoke({
        "topic": state.final_brief.topic,
        "summary": state.final_brief.summary
    })
    print("contextSummary")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    state.context_summary = context_summary.strip()
    return state
