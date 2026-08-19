# Retrieval-Augumented-Generation

## RAG Components

A practical implementation and exploration of the core components used in **Retrieval-Augmented Generation (RAG)** systems.

This project focuses on understanding the individual building blocks of RAG, including **document loading, text splitting, embeddings, vector stores, similarity search, retrieval, prompt engineering, and LLM generation**.

The goal is to understand how each component works independently and how these components come together to build a complete RAG pipeline.

---

## 🚀 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an AI architecture that combines **information retrieval** with **Large Language Models (LLMs)**.

Instead of relying only on the knowledge learned during model training, RAG retrieves relevant information from an external knowledge source and provides it to the LLM as context.

### RAG Architecture

    Documents
        ↓
    Document Loading
        ↓
    Text Splitting
        ↓
    Embeddings
        ↓
    Vector Store
        ↓
    Retrieval
        ↓
    Relevant Context
        ↓
    Prompt
        ↓
    LLM
        ↓
    Generated Answer

---

# 🧩 RAG Components

## 1. 📄 Document Loaders

Document loaders are responsible for loading data from different sources and converting it into a format that can be processed by the RAG pipeline.

### Supported Data Sources

- PDF
- TXT
- CSV
- Markdown
- Word Documents
- Web Pages
- Other structured and unstructured data sources

### Example

    from langchain_community.document_loaders import PyPDFLoader

    loader = PyPDFLoader("document.pdf")
    documents = loader.load()

The loader converts the source document into LangChain `Document` objects.

Each document generally contains:

- Page content
- Metadata

---

## 2. ✂️ Text Splitters

Large documents are divided into smaller pieces called **chunks** before generating embeddings.

Chunking makes documents easier to retrieve and helps the system provide relevant context to the LLM.

### Example

    from langchain_text_splitters import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

### Important Parameters

| Parameter | Description |
|---|---|
| `chunk_size` | Maximum size of each chunk |
| `chunk_overlap` | Amount of overlapping content between chunks |

### Why Chunking Matters

Good chunking is important for retrieval quality.

**If chunks are too small:**

- Important context may be lost.
- Answers may become incomplete.
- Related information may be separated.

**If chunks are too large:**

- Retrieval may become less precise.
- Irrelevant information may be included.
- More tokens may be sent to the LLM.

---

## 3. 🧠 Embeddings

Embeddings convert text into numerical vectors that represent the **semantic meaning** of the text.

For example:

    Text
      ↓
    Embedding Model
      ↓
    Numerical Vector

Example:

    "Python is a programming language"
                    ↓
            Embedding Model
                    ↓
    [0.021, -0.184, 0.742, ...]

Texts with similar meanings generally have similar vector representations.

### Example

    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

Embeddings are generated for both:

- Document chunks
- User queries

This allows the system to compare the semantic similarity between the query and stored documents.

---

## 4. 🗄️ Vector Stores

A vector store stores document embeddings and allows efficient similarity-based searching.

### Popular Vector Stores

- Chroma
- FAISS
- Pinecone
- Qdrant
- Weaviate
- Milvus

### Example with Chroma

    from langchain_chroma import Chroma

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

The basic process is:

    Document Chunk
          ↓
      Embedding
          ↓
     Vector Store

---

## 5. 🔍 Similarity Search

Similarity search finds documents that are semantically related to the user's query.

### Example

    query = "What is machine learning?"

    results = vectorstore.similarity_search(
        query,
        k=3
    )

The `k` parameter determines how many relevant chunks should be returned.

### Similarity Search Flow

    User Query
        ↓
    Query Embedding
        ↓
    Vector Store
        ↓
    Similarity Comparison
        ↓
    Top-K Relevant Documents

---

## 6. 📚 Retrievers

A retriever provides an interface for retrieving relevant documents from a knowledge base.

Instead of manually performing the search every time, a retriever can be used to retrieve relevant chunks.

### Example

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

Retrieve relevant documents:

    docs = retriever.invoke(
        "What is machine learning?"
    )

The retriever returns the most relevant document chunks that can be provided to the LLM.

---

## 7. 📝 Prompt Templates

A prompt template defines how the retrieved context and user's question are presented to the LLM.

### Example

    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using only the provided context.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

A well-designed prompt helps the LLM:

- Use the retrieved information.
- Stay focused on the user's question.
- Reduce irrelevant responses.
- Reduce hallucinations.
- Generate context-aware answers.

---

## 8. 🤖 Large Language Models

The LLM receives the retrieved context along with the user's question and generates the final response.

### Example

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

The LLM is responsible for **generation**, while the retriever is responsible for **retrieval**.

    Retriever
        ↓
    Find Relevant Information
        ↓
    LLM
        ↓
    Generate Answer

---

# 🔄 Complete RAG Pipeline

The complete RAG pipeline can be represented as:

    ┌─────────────────┐
    │    Documents    │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │ Document Loader │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │  Text Splitter  │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │   Embeddings    │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │  Vector Store   │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │    Retriever    │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │ Relevant Context│
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │ Prompt + Query  │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │       LLM       │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │ Generated Answer│
    └─────────────────┘

---

# 📊 Traditional LLM vs RAG

## Traditional LLM

    User Question
          ↓
         LLM
          ↓
    Generated Answer

A traditional LLM primarily relies on the knowledge learned during training.

## RAG

    User Question
          ↓
       Retriever
          ↓
    Relevant Documents
          ↓
        Context
          ↓
         LLM
          ↓
    Grounded Answer

RAG provides the LLM with additional information retrieved from an external knowledge source.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| LangChain | RAG Framework |
| OpenAI | LLM and Embeddings |
| ChromaDB | Vector Storage |
| Git | Version Control |
| GitHub | Repository Management |

---

# 📁 Project Structure

    rag-components/
    │
    ├── data/
    │   ├── sample.pdf
    │   ├── sample.txt
    │   └── sample.csv
    │
    ├── loaders/
    │   └── document_loader.py
    │
    ├── splitters/
    │   └── text_splitter.py
    │
    ├── embeddings/
    │   └── embedding_model.py
    │
    ├── vectorstore/
    │   └── vector_store.py
    │
    ├── retrieval/
    │   └── retriever.py
    │
    ├── generation/
    │   └── llm.py
    │
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    └── README.md

---

# ⚙️ Installation

## 1. Clone the Repository

    git clone <YOUR_REPOSITORY_URL>

Navigate to the project directory:

    cd rag-components

---

## 2. Create a Virtual Environment

    python -m venv venv

### Windows

    venv\Scripts\activate

### macOS / Linux

    source venv/bin/activate

---

## 3. Install Dependencies

    pip install -r requirements.txt

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

    OPENAI_API_KEY=your_api_key_here

> **Important:** Never commit your API key to GitHub.

Add the following to `.gitignore`:

    .env
    venv/
    __pycache__/
    *.pyc

---

# 🧪 Complete RAG Example

The following example demonstrates the complete flow from document loading to answer generation.

    from langchain_community.document_loaders import PyPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_chroma import Chroma

    # Load document
    loader = PyPDFLoader("data/sample.pdf")
    documents = loader.load()

    # Split document
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    # Create embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # Create vector store
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    # Create retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    # User query
    query = "What is this document about?"

    # Retrieve relevant documents
    docs = retriever.invoke(query)

    # Prepare context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    # Create prompt
    prompt = f"""
    Answer the question using only the provided context.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    # Generate response
    response = llm.invoke(prompt)

    print(response.content)

---

# 🎯 Key Concepts Learned

This project provides practical understanding of:

- Document ingestion
- Document loaders
- Document preprocessing
- Text splitting
- Chunk size
- Chunk overlap
- Embedding generation
- Semantic similarity
- Vector stores
- Similarity search
- Retrievers
- Prompt templates
- Context retrieval
- LLM integration
- Retrieval-Augmented Generation
- Grounded question answering

---

# 💡 Real-World Applications

RAG can be used to build:

- 📚 Document Question Answering Systems
- 📄 PDF Question Answering
- 💬 Customer Support Assistants
- 🏢 Enterprise Knowledge Assistants
- 🔎 Semantic Search Systems
- 👨‍💻 Code Documentation Assistants
- 🎓 Educational Assistants
- ⚖️ Legal Document Assistants
- 🏦 Financial Document Analysis
- 🧠 Domain-Specific AI Assistants

---

# 🚧 Future Improvements

Future improvements may include:

- [ ] Add support for additional document formats
- [ ] Experiment with different chunking strategies
- [ ] Compare different embedding models
- [ ] Add metadata filtering
- [ ] Implement hybrid search
- [ ] Add reranking
- [ ] Implement persistent vector storage
- [ ] Add conversational memory
- [ ] Build a Gradio interface
- [ ] Build a Streamlit interface
- [ ] Add retrieval evaluation
- [ ] Add response evaluation
- [ ] Experiment with advanced RAG techniques
- [ ] Add citation support for retrieved documents

---

# 📖 Learning Objective

The main objective of this project is to develop a strong practical understanding of the components that make up a **Retrieval-Augmented Generation system**.

Instead of treating RAG as a single black-box technology, this project breaks the architecture into individual components and demonstrates how each component contributes to the final AI application.

---

# 👩‍💻 Author

**Amina Bibi**

AI Engineer | Generative AI | AI Agents


---

# ⭐ Support

If you find this project useful for learning **RAG, LangChain, and Generative AI**, consider giving the repository a ⭐ on GitHub.
