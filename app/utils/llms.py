# from langchain_community.chat_models import ChatGroq   
from langchain_groq import ChatGroq 
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

def get_groq_llm(model_name="mixtral-8x7b-32768"):
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name=model_name,
        temperature=0.3,
        max_tokens=4096,
    )

def summarize_text(url: str, text: str) -> str:
    if not text or len(text) < 100:
        return "Content too short to summarize."

    llm = get_groq_llm()
    output_parser = StrOutputParser()

    prompt = ChatPromptTemplate.from_template("""
You are a helpful research assistant.

Summarize the following article from the URL in a clear, concise, and factual way. 
Focus on the key insights relevant to the topic. Avoid unnecessary filler, ads, or irrelevant details.

URL: {url}

Content:
{text}

Summary:
""")

    chain = prompt | llm | output_parser

    try:
        return chain.invoke({"url": url, "text": text})
    except Exception as e:
        return f"Summarization failed: {str(e)}"



