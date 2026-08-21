from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

myloader = PyPDFLoader('C:/Retrieval_augumented_generation/Vector_Store/10_Countries_Information.pdf')
file = myloader.load()

mysplitter = RecursiveCharacterTextSplitter(
    chunk_size= 600,
    chunk_overlap=0,
)

chunks = mysplitter.split_documents(file)

myvector_store = Chroma(
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory = 'chroma_data',
    collection_name = 'samplevectors'
)

myvector_store.add_documents(chunks)

