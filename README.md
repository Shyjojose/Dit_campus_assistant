# Dit_campus_assistant
AI-Powered Campus Assistant Chatbot
# 🎓 DIT Campus Chatbot

A **Streamlit-based chatbot** designed for DIT University to answer student and faculty questions related to campus life, academics, events, and services. The chatbot uses a **Retrieval-Augmented Generation (RAG)** pipeline with a FAISS vector database and a locally hosted **Ollama LLM** (e.g., Mistral) for generating responses.

---

## **Features**
- **Local LLM Integration**: Uses the Ollama LLM (e.g., Mistral) running locally for generating responses.
- **FAISS Vector Database**: Efficiently retrieves relevant documents for context-based answers.
- **Streamlit Web Interface**: Provides an easy-to-use interface for interacting with the chatbot.
- **Dynamic Updates**: Supports updating the FAISS database with new text files.

---

## **Project Structure**
- **`chat_ui.py`**: The main Streamlit app that runs the chatbot.
- **`vector_db_create.py`**: Script to create the FAISS vector database from a text file.
- **`update_vb.py`**: Script to update the FAISS vector database with new text files.
- **`rag_engine.py`**: Contains the `load_rag_chain()` function, which initializes the RAG pipeline and connects the FAISS database with the LLM.
- **`deg_campus_data.txt`**: The primary text file containing campus-related data for creating the vector database.
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`readme.md`**: Documentation for the project.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd campus_guide

python3 -m venv dit-chatbot-env
source dit-chatbot-env/bin/activate

ollama pull mistral
ollama serve

Here’s a structured and detailed README.md file for your project:

---

### **README.md**
```markdown
# 🎓 DIT Campus Chatbot

A **Streamlit-based chatbot** designed for DIT University to answer student and faculty questions related to campus life, academics, events, and services. The chatbot uses a **Retrieval-Augmented Generation (RAG)** pipeline with a FAISS vector database and a locally hosted **Ollama LLM** (e.g., Mistral) for generating responses.

---

## **Features**
- **Local LLM Integration**: Uses the Ollama LLM (e.g., Mistral) running locally for generating responses.
- **FAISS Vector Database**: Efficiently retrieves relevant documents for context-based answers.
- **Streamlit Web Interface**: Provides an easy-to-use interface for interacting with the chatbot.
- **Dynamic Updates**: Supports updating the FAISS database with new text files.

---

## **Project Structure**
- **`app.py`**: The main Streamlit app that runs the chatbot.
- **`vb.py`**: Script to create the FAISS vector database from a text file.
- **`update_vb.py`**: Script to update the FAISS vector database with new text files.
- **`rag_engine.py`**: Contains the `load_rag_chain()` function, which initializes the RAG pipeline and connects the FAISS database with the LLM.
- **`deg_campus_data.txt`**: The primary text file containing campus-related data for creating the vector database.
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`readme.md`**: Documentation for the project.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd campus_guide
```

### **2. Set Up a Virtual Environment**
```bash
python3 -m venv dit-chatbot-env
source dit-chatbot-env/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Pull and Run the Ollama Model**
Ensure the Ollama server is installed and running locally:
```bash
ollama pull mistral
ollama serve
```

---

## **How to Run the Project**

### **1. Create the FAISS Vector Database**
Run the `vb.py` script to create the FAISS database from the `deg_campus_data.txt` file:
```bash
python vb.py
```

### **2. Update the FAISS Database (Optional)**
If you have new data to add, use the `update_vb.py` script:
```bash
python update_vb.py
```

### **3. Run the Streamlit App**
Start the chatbot by running the Streamlit app:
```bash
streamlit run app.py
```

---

## **How It Works**
1. **FAISS Database**:
   - The `vector_db_create.py` script splits the text data into chunks, generates embeddings using the Ollama LLM, and stores them in a FAISS vector database (`faiss_db_dit`).

2. **RAG Pipeline**:
   - The `rag_engine.py` file initializes the RAG pipeline by:
     - Loading the FAISS database.
     - Using the Ollama LLM to generate responses based on retrieved documents.
     - Defining a prompt template for context-based answers.

3. **Streamlit Interface**:
   - The `app.py` file provides a web interface where users can ask questions. The app retrieves relevant documents from the FAISS database and generates responses using the LLM.

---

## **Dependencies**
The project requires the following Python libraries:
- `streamlit`
- `langchain`
- `langchain-ollama`
- `langchain-community`
- `faiss-cpu`
- `scikit-learn`
- `umap-learn`
- `plotly`
- `matplotlib`

Install them using:
```bash
pip install -r requirements.txt
```

---

## **Example Usage**
1. **Ask a Question**:
   - Open the Streamlit app and ask a question like:
     ```
     What are the facilities available on campus?
     ```

2. **Response**:
   - The chatbot retrieves relevant information from the FAISS database and generates a response using the LLM.

---

## **Troubleshooting**

### **1. FAISS Database Issues**
- If the FAISS database is corrupted or missing, delete the `faiss_db_dit` directory and recreate it using `vb.py`.

### **2. Ollama Server Not Running**
- Ensure the Ollama server is running locally:
  ```bash
  ollama serve
  ```

### **3. Missing Dependencies**
- Install missing dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

---

## **Future Enhancements**
- Add support for remote hosting of the LLM server.
- Implement user authentication for secure access.
- Expand the chatbot's knowledge base with additional datasets.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**
- **LangChain**: For providing tools to build the RAG pipeline.
- **Ollama**: For the local LLM support.
- **FAISS**: For efficient vector search capabilities.
```

---

### **How to Use This README.md**
1. Save the content in a file named README.md in your project directory:
   ```bash
   /Users/shyjojose/Desktop/campus_guide/README.md
   ```

2. Push it to your GitHub repository:
   ```bash
   git add README.md
   git commit -m "Add project documentation"
   git push
   ```

Let me know if you need further assistance!
