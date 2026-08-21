from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document

myloader = PyPDFLoader('C:/Retrieval_augumented_generation/Vector_Store/10_Countries_Information.pdf')
file = myloader.load()

mysplitter = RecursiveCharacterTextSplitter(
    chunk_size= 7000,
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
print(embedings)

## To see Docs from vector store
docs = myvector_store.get(include=['documents'])
print(docs)


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

#docs = myvector_store.get(include=['documents'])
#print(docs)

#Delete document
myvector_store.delete(ids= ['ef1a94d5-dc30-4fa5-92b8-b1a913de650f', '484f9824-ce07-4fcf-931b-c0cc87679e83', '1bdf5e6a-86e2-4f4e-a48b-c5244ada3d61', '57767b94-3ca9-45a1-a068-bac0b25e85eb', '0e3bd92b-b354-4edc-8fa9-8e8e1156422d', '7dcd36b7-12b5-4cea-9968-b8f032cb8374', 'fc86a5f3-c91f-4fc4-8b3b-0d09b9a094b4', 'a9452671-c340-4f52-ad3d-cde65535b538', '7b5b2530-15ad-4abe-9246-e41d771ab31f', 'da09baa1-41da-4d02-b9a9-927fbd32ef94', '084781ae-85e3-45c9-beca-2dde88d42728', '80f38233-d986-453c-ab57-86b159b08bf6', '391d561d-ef36-4339-82fd-21156b0494e6', 'b5007faa-e17b-4a9e-8e5c-5c72afa55e15', 'e854dee0-818a-450f-992d-a91daf027a9b', '6b7c1147-3230-45ce-8e22-7f5b813e272d', '54b324ab-5850-474e-85f6-9c1f7fcdd317', '37089e04-6f55-4e3b-a369-9a7f5cbce814', 'ccee148b-9216-48dc-9be2-0f91e7381063', 'b1f7731a-8460-4946-9a81-b5dea0f1ea88', '2228a1eb-31de-4a3a-9e03-2cc6f45e7627'])

print('after deleting \n \n')

docs = myvector_store.get(include=['documents'])
print(docs)
