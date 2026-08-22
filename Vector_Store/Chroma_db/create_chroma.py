from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

myvector_store = Chroma(
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory = 'chroma_data',
    collection_name = 'samplevectors'
)

