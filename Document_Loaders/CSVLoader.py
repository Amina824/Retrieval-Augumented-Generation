from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('C:\RETRIEVAL_AUGUMENTED_GENERATION\lang_data.csv')
chunks = loader.load()

print(chunks)