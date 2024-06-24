# Import the load_dotenv function from the dotenv package
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


import os

# Load the variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("API_KEY")

# Build LLM Model --------------------------------------
llm = GooglePalm(google_api_key=api_key, temperature=0.5)


# Get word embeddings using google palm embedding
google_palm_embeddings = GooglePalmEmbeddings(google_api_key=api_key)


def create_context(text):

    # make our text as Document type
    # Create a Document object from the context_data string
    document_data = [Document(page_content=text, metadata={"source": "context"})]

    # create vector db for store word embeddings ----------------
    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(
        documents=document_data, embedding=google_palm_embeddings
    )

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    # create memory instance for store the context ----------------------
    memory = ConversationBufferWindowMemory(k=5)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly give most approprate answers most matched to context.If Context is  about quections like assignment dont repeat quection again in result.
    if Context defined some quections and user asked that quections please give answer for that quections. 

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        memory=memory,
        return_source_documents=False,
        chain_type_kwargs=chain_type_kwargs,
    )

    return chain


def get_response(chain, prompt):
    return chain.run(prompt)
