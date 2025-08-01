from langchain_core.prompts import ChatPromptTemplate
# from langchain.output_parsers import StrOutputParser
from langchain_core.output_parsers import StrOutputParser

from app.utils.llms import get_groq_llm

def planner_node(state):
    prompt = ChatPromptTemplate.from_template("""
    Given the research topic "{topic}" and depth level {depth}, create 3 specific research steps or sub-questions to explore.
    """)
    
    llm = get_groq_llm("llama3-70b-8192")
    chain = prompt | llm | StrOutputParser()

    steps = chain.invoke({"topic": state.topic, "depth": state.depth})
    # state.planning_steps = steps.strip().split("\n")
    state.planning_steps = [s.strip("- ").strip() for s in steps if s.strip()]
    return state
