# create_vector_db.py

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_vector_db():
    loader = TextLoader("deg_campus_data.txt", encoding="utf-8")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    documents = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="mistral")

    vector = FAISS.from_documents(documents, embeddings)
    vector.save_local("faiss_db_dit")
    print("✅ Vector database saved to 'faiss_db_dit'")

if __name__ == "__main__":
    create_vector_db()
    print("🚀 Creating vector database...")