from ingest import ingest
from embed import embed
from retrieve import retrieve
from generate import generate
from verify import verify

def main():
    q=input("enter your question? ")
    folder_path=input("enter your file path: ")
    folder=ingest(folder_path)
    echunk=embed(folder)
    schunk=retrieve(echunk, q)
    answer=generate(schunk, q)
    results=verify(schunk, answer)
    print("\nRESULTS:")
    print(f"Question:{q}\n")
    print(f"Answer:{answer}\n")
    print(" VERIFICATION:")
    for r in results:
        print(f"Claim:{r['claim'][:50]}...")
        print(f"Score:{r['score']}")
        print(f"Source:{r['source']}\n")

if __name__ == "__main__":
    main()