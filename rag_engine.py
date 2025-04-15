import os
from langchain_ollama import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

def load_rag_chain():
    # Define the embedding model
    embeddings = OllamaEmbeddings(model="mistral")

    # Load or create the FAISS database
    if os.path.exists("faiss_db_dit"):
        print("Loading existing FAISS database...")
        vector = FAISS.load_local("faiss_db_dit", embeddings, allow_dangerous_deserialization=True)
    else:
        print("Creating a new FAISS database...")
        loader = TextLoader("deg_campus_data.txt", encoding="utf-8")
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        documents = text_splitter.split_documents(docs)

        vector = FAISS.from_documents(documents, embeddings)
        vector.save_local("faiss_db_dit")
        print("FAISS database created and saved.")

    # Create retriever
    retriever = vector.as_retriever()

    # Define LLM
    llm = OllamaLLM(model="mistral", temperature=0)

    # Define prompt template
    prompt = ChatPromptTemplate.from_template("""
    You are DIT CampusBot, a helpful and respectful virtual assistant for DIT University. 
Your role is to answer student and faculty questions related to campus life, academics, events, and services at DIT University, using only the provided context.

If a user asks a question that is:
- Not related to DIT University, its curriculum, facilities, events, or academic life
- Outside the context provided
Then respond with: 
"⚠️ Sorry, this information is not available in the current context. Your request will be reviewed."

If the user enters any offensive, abusive, or inappropriate input:
- Warn them by saying: 
"🚫 Offensive or inappropriate queries are not tolerated. This conversation may be reviewed by campus authorities and action may be taken as per university policy."

<context>
{context}
</context>

Question: {input}
    """)

    # Create document chain and retrieval chain
    document_chain = create_stuff_documents_chain( llm, prompt)
    return create_retrieval_chain(retriever, document_chain)