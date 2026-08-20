from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

myloader = PyPDFLoader('C:/Retrieval_augumented_generation/Vector_Store/10_Countries_Information.pdf')
file = myloader.load()

mysplitter = RecursiveCharacterTextSplitter(
    chunk_size= 600,
    chunk_overlap=0,
)

chunks = mysplitter.split_documents(file)
print(chunks[0].page_content)
print(chunks[1].page_content)