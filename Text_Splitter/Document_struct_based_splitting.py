from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders import TextLoader

loader = TextLoader(r'C:\Retrieval_augumented_generation\README.md',
                    encoding = 'utf-8')
file = loader.load()

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.MARKDOWN,
    chunk_size = 500,
    chunk_overlap = 50,
)

chunks = splitter.split_documents(file)
print(chunks)
print(len(chunks))
