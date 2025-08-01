from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.state import GraphState, SourceSummary
from app.utils.llms import get_groq_llm
from app.utils.content_fetcher import fetch_url_text

# Truncate to limit token load and hallucination risk
def truncate_content(text: str, max_chars: int = 4000) -> str:
    return text[:max_chars] if len(text) > max_chars else text

def summarizer_node(state: GraphState) -> GraphState:
    llm = get_groq_llm("llama3-70b-8192")

    prompt = ChatPromptTemplate.from_template("""
You are an expert summarizer.

Given the following web content, generate a **concise and insightful summary** in **3 to 5 sentences max**. 
Avoid copying text. Capture only the key points, important insights, or takeaways in your own words.

---

Source URL: {source_url}

Content:
{content}

---
Summary:
""")

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    summaries = []
    for source_url in state.sources:
        try:
            content = fetch_url_text(source_url)

            if not content or content.strip() == "":
                print(f"⚠️ Skipping empty content for {source_url}")
                continue

            truncated_content = truncate_content(content)

            summary = chain.invoke({
                "source_url": source_url,
                "content": truncated_content
            })

            summaries.append(SourceSummary(
                source_url=source_url,
                content=truncated_content,
                summary=summary.strip()
            ))

            print(f"Summarized: {source_url}")
        except Exception as e:
            print(f"Error processing {source_url}: {e}")
            continue

    state.summaries = summaries
    print("Total Summaries Generated:", len(summaries))
    print(summaries)
    return state
