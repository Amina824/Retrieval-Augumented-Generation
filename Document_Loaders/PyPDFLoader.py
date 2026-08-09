from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:/RETRIEVAL_AUGUMENTED_GENERATION/Document_Loaders/loaderdata/lang_data.pdf')
chunks = loader.load()
print(chunks)