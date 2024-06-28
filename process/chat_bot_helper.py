# Import the load_dotenv function from the dotenv package
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains import LLMChain


import os

# Load the variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("API_KEY")

# Build LLM Model --------------------------------------
llm = GooglePalm(google_api_key=api_key, temperature=0.7)


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
    retriever = vectordb.as_retriever(score_threshold=0.8)

    # create memory instance for store the context ----------------------
    memory = ConversationBufferWindowMemory(k=5)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly give most appropriate answers.If Context is  about quections like assignment don't repeat quection again in response.
    if Context defined some quections and user asked that quections please give answer for that quections.  Give answers more natural.

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


if __name__ == "__main__":
    text = "CS2023 - Data Structures and Algorithms Take Home Assignment Week 5 - Basic Data Structures March , 2023 You are required to answer the below questions and submit a PDF to the submission link provided under this week before the deadline ( no extensions will be provided ) . You can either write / type your answers , but either way your answers should be readable . Question 1 Explain briefly what a double linked list and a circular linked list is ? Note : Please use diagrams in your explanations Question 2 Write pseudo codes for the operations of a single linked list . Question 3 How can you implement a stack and a queue using a linked list ? Note : Explain how you would do it and also write pseudo codes for all the operations ."
    chain = create_context(text)
    prompt = "Give answers for this assignment all quections?"
    response = get_response(chain, prompt)
    print(response)


def get_normal_chain():
    # Define your prompt template
    normal_prompt_template = PromptTemplate(
        input_variables=["query"],
        template="Answer the following question based on your knowledge: {query}",
    )

    # Initialize the RunnableSequence
    normal_chain = LLMChain(llm=llm, prompt=normal_prompt_template)
    return normal_chain
