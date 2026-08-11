# Retrieval-Augumented-Generation

## RAG Components

A practical implementation of the core components used in a **Retrieval-Augmented Generation (RAG)** system.

This project demonstrates the complete RAG pipeline, including **document loading, text splitting, embeddings, vector storage, similarity search, retrieval, and LLM-based response generation**.

The goal is to understand how individual RAG components work together to build AI applications that retrieve relevant information from external knowledge sources before generating an answer.

---

## 🚀 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an architecture that combines information retrieval with Large Language Models (LLMs).

Instead of relying only on the knowledge stored inside an LLM, RAG retrieves relevant information from an external knowledge base and provides that information as context to the LLM.

### Basic RAG Flow

```text
Documents
    ↓
Document Loading
    ↓
Text Splitting
    ↓
Embeddings
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Relevant Context
    ↓
LLM
    ↓
Generated Answer
