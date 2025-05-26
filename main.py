import  streamlit as st
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
import os
import pickle
import time
from langchain.chains import RetrievalQAWithSourcesChain
from schedular import job
from langchain_huggingface import HuggingFaceEmbeddings


st.sidebar.title(" Equity Research Tool 📈")

st.markdown("""
## 👋 Welcome to the **Equity Research Tool** 📈

This tool helps you stay informed with the **latest financial news** from trusted sources like **Moneycontrol**.  
Here's what you can do:

- 📰 Automatically fetch the **latest news article URLs from MoneyControl website**.
- 🤖 Ask any **finance-related question**, and our AI will read through the news and provide a **contextual answer**.
- 📚 Get the **source links** for transparency and verification.

**How to use:**
1. Click the `Process URLs` button in the sidebar to fetch and process today's top financial news.
2. Type your question below (e.g., _"What’s the latest update on IPOs?"_).
3. Get quick, AI-powered answers with trusted sources.

Stay informed. Stay ahead. 🚀
""")

acess = st.secrets[api_key]
# getpass()

os.environ["GROQ_API_KEY"] = acess
# urls=get_urls("https://www.moneycontrol.com/")
urls = []


process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faisss_store.pkl"

main_placeholder = st.empty()
llm = ChatGroq(temperature=0 ,model_name="llama3-8b-8192")

if st.sidebar.button("Clear Cached VectorStore"):
    if os.path.exists(file_path):
        os.remove(file_path)
        st.success("Vector store cleared. Click 'Process URLs' again to reprocess.")

if process_url_clicked:
    job()
    with open('daily_news_links.txt','r',encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("http"):
                urls.append(line)

        urls = [url for url in urls if url.strip()]
        if not urls:
            st.warning("Please enter at least one valid URL.")

        # load data
        loader = UnstructuredURLLoader(urls=urls)

        main_placeholder.text("Data Loading...Started...✅✅✅")
        try:
            data = loader.load()
        except Exception as e:
            st.error(f"Error loading URLs: {e}")
        # split data
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        docs = text_splitter.split_documents(data)
        # create embeddings and save it to FAISS index
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        time.sleep(2)

        # Save the FAISS index to a pickle file
        with open(file_path, "wb") as f:
            pickle.dump(vectorstore, f)
query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain.invoke({"question": query})
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)
