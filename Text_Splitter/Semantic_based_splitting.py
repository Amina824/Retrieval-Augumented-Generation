from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

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

splitter = SemanticChunker(
    OpenAIEmbeddings(model="text-embedding-3-small"),
    breakpoint_threshold_type= 'standard_deviation',
    breakpoint_threshold_amount=1

)

chunks = splitter.create_documents([text])
print(chunks)