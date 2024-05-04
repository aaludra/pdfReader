from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = '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'


def readPdf(path):
    pdfreader = PdfReader(path)

    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    # Download embeddings from OpenAI
    embeddings = OpenAIEmbeddings()

    document_search = FAISS.from_texts(texts, embeddings)

    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    return document_search, chain


def queryPdf(document_search, chain, query):
    docs = document_search.similarity_search(query)
    return chain.run(input_documents=docs, question=query)
