from create_chroma import myvector_store
## Similarity Search
## k is how many similar documents u want as output related to query
result = myvector_store.similarity_search(
    query='which country is famous for automobiles',
    k=1
)
print('query result is', result[0].page_content)


##Similarity Search with Similarity Score
score = myvector_store.similarity_search_with_score(
    query='which country is famous for automobiles',
    k=1
)
print('query result with score  is', score)
