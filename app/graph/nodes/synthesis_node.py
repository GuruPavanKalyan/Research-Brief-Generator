from app.state import GraphState, FinalBrief
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.utils.llms import get_groq_llm

def synthesis_node(state: GraphState) -> GraphState:
    llm = get_groq_llm("llama3-70b-8192")

    # Step 1: Prepare the content
    combined_summaries = "\n\n".join(
        f"Source: {s.source_url}\nSummary: {s.summary}" for s in state.summaries
    )

    prompt = ChatPromptTemplate.from_template("""
You will receive a synthesized research brief.

Reformat it into:
1. A clean markdown summary
2. A bullet-pointed list of 5–7 key highlights
Depth level: {depth}
Brief:
{combined_summaries}

Respond in this format:

## Summary

<Markdown-formatted brief>

## Key Highlights

- point 1
- point 2
- ...
""")

    chain = prompt | llm | StrOutputParser()

    # Step 3: Generate final brief
    synthesized_summary = chain.invoke({
        "topic": state.topic,
        "depth": state.depth,
        "combined_summaries": combined_summaries
    })

    # Step 4: Create FinalBrief object
    final_brief = FinalBrief(
        topic=state.topic,
        depth=state.depth,
        user_id=state.user_id,
        summary=synthesized_summary,
        references=state.summaries
    )

    return state.copy(update={"final_brief": final_brief})
