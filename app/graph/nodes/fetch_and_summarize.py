from app.state import GraphState
from app.utils.content_fetcher import fetch_url_text
from app.utils.llms import summarize_text  

def fetch_and_summarize_node(state: GraphState) -> GraphState:
    summarized_results = []

    for url in state.sources:
        try:
            content = fetch_url_text(url)
            summary = summarize_text(content, topic=state.topic)
            summarized_results.append({
                "source_url": url,
                "content": content,
                "summary": summary
            })
        except Exception as e:
            print(f"Failed for {url}: {e}")
    
    return state.copy(update={"summaries": summarized_results})
