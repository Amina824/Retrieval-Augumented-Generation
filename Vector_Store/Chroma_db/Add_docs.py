from create_chroma import myvector_store
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document

myloader = PyPDFLoader('C:/Retrieval_augumented_generation/Vector_Store/10_Countries_Information.pdf')
file = myloader.load()

mysplitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap=0,
)

chunks = mysplitter.split_documents(file)



## Adding docs to vector store--> Vecor store will assign ids to each doc
myvector_store.add_documents(chunks)


## To see ids and embeddings(vectors) of docs(chunks)
embedings = myvector_store.get(include=['embeddings'])
print(embedings)

## To see Docs from vector store
docs = myvector_store.get(include=['documents'])
print(docs)


## To see metadata of docs from vector store
metadata = myvector_store.get(include=['metadatas'])
print(metadata)




