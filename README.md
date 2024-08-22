# AI-PDF Reader - Multi-RAG Architecture LLM Project

## Description

This project implements a multi-RAG (Retrieval-Augmented Generation) architecture using Google's PaLM LLM (Language Model) and the LangChain framework. The application is designed to allow users to upload one or more PDF documents, which are then processed and indexed using the Faiss vector database. Once the documents are indexed, users can ask questions related to the content of the PDFs, and the system will provide accurate, context-aware answers based on the retrieved information.

The main objective of this project is to leverage advanced NLP (Natural Language Processing) techniques to build an interactive and efficient question-answering system that enhances document comprehension and retrieval capabilities. The frontend of the application is built using Streamlit, offering a user-friendly interface for document upload and query submission.

## What is Multi-RAG Architecture?

Multi-RAG (Multi-Retrieval-Augmented Generation) is an advanced NLP architecture that combines the strengths of both retrieval-based and generation-based models. In this architecture, the system first retrieves relevant information from a large corpus (e.g., PDF documents) using a vector database like Faiss. This retrieved information is then fed into a generative language model (e.g., Google's PaLM) to generate accurate and contextually relevant answers to user queries.

The multi-RAG architecture ensures that the generated responses are not only based on the language model's training but are also grounded in the specific content of the provided documents, resulting in more precise and contextually aware answers.

## Technology Stack

- **Google PaLM LLM**: Utilized for generating context-aware responses based on retrieved document content.
- **LangChain Framework**: Provides the necessary components for building the multi-RAG architecture, including document processing, retrieval, and integration with LLMs.
- **Faiss Vector Database**: Used for efficient and scalable document indexing and retrieval.
- **Streamlit**: A Python-based framework used to create the frontend interface, enabling users to upload PDFs and ask questions interactively.

## Features

- **PDF Upload**: Users can upload one or more PDF documents to the system.
- **Document Processing**: The uploaded PDFs are processed and indexed using the Faiss vector database.
- **Question Answering**: Users can submit questions related to the content of the uploaded PDFs. The system retrieves relevant sections from the documents and generates contextually accurate answers using Google's PaLM LLM.
- **Multi-Document Support**: The application supports querying across multiple PDFs, making it a versatile tool for research and information retrieval.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- LangChain
- Faiss
- Google PaLM API access

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi-rag-architecture-llm.git
   cd multi-rag-architecture-llm

