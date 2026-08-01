from sentence_transformers import SentenceTransformer
from ingest import ingest
def embed(chunk):
    model=SentenceTransformer("all-MiniLM-L6-v2")
    for file in chunk:
        file["embeddings"]=model.encode(file["content"])
    return chunk

def main():
    folder=input("enter a folder path")
    chunks=ingest(folder)
    embedded_chunks=embed(chunks)
    return embedded_chunks
if __name__=="__main__":
    result=main()
    print(f"embedded {len(result)} files")
    for file in result:
        print(file["embeddings"])