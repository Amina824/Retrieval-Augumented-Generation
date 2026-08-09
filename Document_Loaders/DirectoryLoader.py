from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='C:/RETRIEVAL_AUGUMENTED_GENERATION/Document_Loaders/loaderdata/Directory_lang',
    glob='*.pdf',
    loader_cls=PyPDFLoader
    )

chunks = loader.load()
print(chunks)