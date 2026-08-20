from langchain_text_splitters import CharacterTextSplitter

text = """
# LangChain

## Introduction

LangChain is an open-source framework used to build applications powered by Large Language Models (LLMs). It helps developers connect an LLM with external data, tools, APIs, databases, and conversation history.

LangChain is commonly used to build AI chatbots, question-answering systems, RAG applications, AI agents, and automation workflows.

## What is an LLM?

An LLM (Large Language Model) is an AI model that can understand and generate human language. Examples include GPT models, Claude, Gemini, and other language models.

LangChain does not replace the LLM. Instead, it provides tools and structures that make it easier to use an LLM inside an application.

## Main Components of LangChain

### 1. Models

Models are the AI systems that generate responses.

LangChain can work with different types of models, including:

* Chat models
* Language models
* Embedding models

Example:

A user asks, "What is machine learning?"

The LLM processes the question and generates an answer.
"""

splitter = CharacterTextSplitter(
    chunk_size= 50,
    chunk_overlap= 10,
    separator = "",
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])