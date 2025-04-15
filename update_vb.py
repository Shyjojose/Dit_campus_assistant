from langchain_community.document_loaders import TextLoader
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load the new text
loader = TextLoader("new_info.txt", encoding="utf-8")
docs = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
new_documents = text_splitter.split_documents(docs)

# Load existing DB and embedding model
embeddings = OllamaEmbeddings(model="mistral")
db = FAISS.load_local("faiss_db_dit", embeddings, allow_dangerous_deserialization=True)

# Add new docs
db.add_documents(new_documents)

# Save the updated DB
db.save_local("faiss_db_dit")

print("✅ New information successfully added to FAISS DB.")
print("🚀 Vector database updated with new information.")