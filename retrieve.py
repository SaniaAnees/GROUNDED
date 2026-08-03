import numpy as np
from ingest import ingest
from embed import embed
from sentence_transformers import SentenceTransformer
def retrieve(embedded_chunk,question):
    model=SentenceTransformer("all-MiniLM-L6-v2")
    emb_que=model.encode(question)
    for file in embedded_chunk:
        file["similarity_score"]=np.dot(file['embeddings'], emb_que) / (np.linalg.norm(file['embeddings']) * np.linalg.norm(emb_que))
    return sorted(embedded_chunk,key=lambda x: x['similarity_score'],reverse=True)[:5]
        


def main():
    q=input("Enter your question : ")
    folder_path=input("Enter your file path : ")
    folder=ingest(folder_path)
    echunk=embed(folder)
    schunk=retrieve(echunk,q)
    print(f"Top 5 results for: {q}")
    for result in schunk:
        print(f"File: {result['filename']}, Similarity: {result['similarity_score']}")
    return schunk
    
if __name__=="__main__":
    main()