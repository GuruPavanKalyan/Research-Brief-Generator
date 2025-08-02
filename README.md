# 📘 Context-Aware Research Brief Generator

This project is an intelligent LangGraph-based pipeline that automates the generation of concise research briefs from a set of online sources. It leverages LLMs, LangChain components, LangSmith tracing, and modular LangGraph nodes to ensure explainability, observability, and scalability.

---

## ✨ Features

- 🔎 **Search Node**: Queries a user topic and fetches relevant content from the web.
- 🧠 **Summarizer Node**: Generates concise 3–5 sentence summaries for each source.
- 🧩 **Synthesizer Node**: Combines individual summaries into a final coherent research brief.
- 🧠 **Context Summarization (Planned)**: Reduces large input content into manageable context windows.
- ✅ **Structured Output**: Returns structured results using Pydantic models.
- 📊 **LangSmith Tracing**: Integrated with LangSmith for observability, cost analysis, and LLM chain insights.
- 🛠️ **FastAPI Interface**: Interact with the pipeline via REST API.
- 🧪 **Testable & Modular**: Each component is isolated for easy testing and reuse.
- 🚀 **Environment-driven Deployment**: All secrets and config are managed through `.env`.

---

## 📦 Installation
- git clone https://github.com/your-username/research-brief-agent.git

- cd research-brief-agent

- python -m venv venv

- source venv/bin/activate  # or .\venv\Scripts\activate on Windows
- pip install -r requirements.txt


## Set your environment variables in .env:

- OPENAI_API_KEY=...
- GROQ_API_KEY=...
- LANGCHAIN_TRACING_V2=true
- LANGCHAIN_PROJECT=my-research-agent
- SERPAPI_API_KEY=...

## 📁 Project Structure
  ![alt text](image-2.png)

## 🧪 Usage
### CLI
- python app/cli/main.py --topic "Impact of AI on Education" --depth 1
### FastAPI
- {
  "topic": "AI in Healthcare",
  "depth": 2,
  "follow_up": true,
  "user_id": "guru123"
}

## 🧠 Node Overview
![alt text](image-1.png)

## 📊 Observability

- Integrated with LangSmith for tracing
- Token usage and cost tracking per run
- Logging for each node's input/output state
- <img width="1899" height="853" alt="image" src="https://github.com/user-attachments/assets/f0bdea3b-9d16-4038-8c6b-5a2d2dfb6106" />


## 🧩 Dependencies

- LangGraph
- LangChain
- FastAPI
- Pydantic
- Groq SDK
- Serpapi

## 🛠 TODO
- Add RAG-based document ingestion
- Enable image + text multimodal input
- Frontend (React interface)
- SerpAPI key dependent response

## DEMO
- https://www.loom.com/share/43f06adc27c74369baf0b3a4eda3c6e4?t=625&sid=8c96a97b-bc0d-40a3-adf9-fc2cce2636a5

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

## 📄 License
MIT © 2025 Guru Pavan Kalyan

## 📬 Contact
- Guru Pavan Kalyan Bandaru
- pavankalyanbandaru6@gmail.com
