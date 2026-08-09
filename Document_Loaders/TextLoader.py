from langchain_community.document_loaders import TextLoader

loader=TextLoader("C:/RETRIEVAL_AUGUMENTED_GENERATION/Document_Loaders/loaderdata/lang_data.txt")

docs=loader.load()
print(docs)
print