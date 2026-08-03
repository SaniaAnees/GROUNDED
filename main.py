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
    
    print("\n" + "="*60)
    print("VERIFICATION RESULTS")
    print("="*60)
    print(f"\nQuestion: {q}\n")
    print(f"Answer: {answer[:150]}...\n")
    
    print("Top 3 Claims:")
    for i, r in enumerate(results[:3], 1):
        claim = r['claim'][:60] + "..." if len(r['claim']) > 60 else r['claim']
        score = f"{r['score']:.2f}"
        status = "✓" if float(r['score']) > 0.7 else "✗"
        print(f"\n{i}. {claim}")
        print(f"   Score: {score} {status}")

if __name__ == "__main__":
    main()