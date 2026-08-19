from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders import TextLoader

loader = TextLoader('C:/Retrieval_augumented_generation/README.md',
                    encoding='utf-8')
markdown = loader.load()

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=10
)

result = splitter.split_documents(markdown)
print(result)