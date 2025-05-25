# 📈 Equity Research Tool

An interactive Streamlit-based application that allows users to perform real-time analysis on financial news articles. It uses LangChain, Groq's LLaMA 3 model, HuggingFace embeddings, and FAISS to answer user questions based on the content of URLs provided.

---

## 🚀 Features

- 🔗 Accepts up to 3 financial news URLs
- 🧠 Uses LLaMA 3 via Groq for intelligent question answering
- 🧾 Splits and embeds content using HuggingFace transformers
- 🧱 Stores embeddings with FAISS vector store
- 🔍 Enables question-answering with document references
- 📄 Displays source links used to generate the response
- 💾 Caches embeddings locally for quick reuse

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | [LangChain](https://github.com/langchain-ai/langchain) |
| LLM | [Groq LLaMA 3 (8B)](https://groq.com/) |
| Embeddings | [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) |
| Vector Store | [FAISS](https://github.com/facebookresearch/faiss) |
| UI | [Streamlit](https://streamlit.io/) |
| Loader | `UnstructuredURLLoader` from LangChain |

---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rutikshindepatil21/EquityResearchTool.git
cd EquityResearchTool
