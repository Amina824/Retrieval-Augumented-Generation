from langchain_community.document_loaders import TextLoader

loader=TextLoader("C:/RETRIEVAL_AUGUMENTED_GENERATION/loaderdata/lang_data.txt")

chunks=loader.load()
print(chunks)