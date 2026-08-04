from chunker import main as get_chunks
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

collection_name = "heinz_handbooks"

embeddings = OpenAIEmbeddings( 
    model="text-embedding-3-large", #calls the embedding model from OpenAI
    openai_api_key=os.getenv("OPENAI_API_KEY") #secret API key for accessing openAI library
)

chunks = get_chunks() #imported function from chunker.py that created all the chunks 

#client = QdrantClient(url="http://localhost:6333") 


#deletes the previously stored collection so that vectors are not repeated 
client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
) 
if client.collection_exists(collection_name):
    client.delete_collection(collection_name)
    print(f"Deleted existing collection '{collection_name}'")



doc_store = QdrantVectorStore.from_documents( #stores the chunks into qdrant vector store
    chunks, #created chunks from 'get_chunks()' function
    embeddings, #the OpenAI embedding model stored in variable embeddings
    #url="http://localhost:6333", #qdrant url
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    prefer_grpc=True,
    collection_name=collection_name,  #name given to the embedding storage
)

print(f"Stored {len(chunks)} chunks in Qdrant.")
