from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document

myloader = PyPDFLoader('C:/Retrieval_augumented_generation/Vector_Store/10_Countries_Information.pdf')
file = myloader.load()

mysplitter = RecursiveCharacterTextSplitter(
    chunk_size= 600,
    chunk_overlap=0,
)

chunks = mysplitter.split_documents(file)


## Creating Vector Store
myvector_store = Chroma(
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory = 'chroma_data',
    collection_name = 'samplevectors'
)

## Adding docs to vector store--> Vecor store will assign ids to each doc
myvector_store.add_documents(chunks)


## To see ids and embeddings(vectors) of docs(chunks)
embedings = myvector_store.get(include=['embeddings'])
#print(embedings)

## To see Docs from vector store
docs = myvector_store.get(include=['documents'])
 #print(docs)


## To see metadata of docs from vector store
metadata = myvector_store.get(include=['metadatas'])
#print(metadata)


## Similarity Search
## k is how many similar documents u want as output related to query
result = myvector_store.similarity_search(
    query='which country is famous for automobiles',
    k=1
)
#print('query result is', result[0].page_content)


##Similarity Search with Similarity Score
score = myvector_store.similarity_search_with_score(
    query='which country is famous for automobiles',
    k=1
)
#print('query result with score  is', score)

##update_existing documents
updated_doc1 = Document(
    page_content= ('Turkey is beautiful country. Its famous for its touarism and have many masjids'),
    metadata = {'region': 'Asia'}
)

myvector_store.update_document(document_id = '5ac0e46a-f9ca-4057-b9e8-360958e0f808', document= updated_doc1 )

docs = myvector_store.get(include=['documents'])
#print(docs)

#Delete document
my

