from create_chroma import myvector_store
from langchain_core.documents import Document

##update_existing documents
updated_doc1 = Document(
    page_content= ('Turkey is beautiful country. Its famous for its touarism and have many masjids'),
    metadata = {'region': 'Asia'}
)

myvector_store.update_document(document_id = 'b894fe95-91b8-4858-af5b-95088a7df4fb', document= updated_doc1 )

#docs = myvector_store.get(include=['documents'])
#print(docs)

#Delete document
myvector_store.delete(ids= ['084f4107-7dd5-47ef-9cab-9d2ba4838aa7', '2687f0a8-8dea-4d58-9e72-ba35f88a1d3b'])

print('after deleting \n \n')

docs = myvector_store.get(include=['documents'])
print(docs)
