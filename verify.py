from sentence_transformers import CrossEncoder
from ingest import ingest
from embed import embed
from retrieve import retrieve
from generate import generate
def verify(schunk, answer):
    try:
        model = CrossEncoder('cross-encoder/qnli-distilroberta-base')
        claims = answer.split('.')
        claims = [c.strip() for c in claims if c.strip()]
        results = []
        for claim in claims:
            for chunk in schunk:
                score=float(model.predict([[claim,chunk['content']]])[0])
                results.append({"claim": claim, "score": score, "source": chunk['filename']})
        return results
    except Exception as e:
        print(f"Error: {e}")
        return "No answer generated"  


def main():
    q=input("enter your question?")
    folder_path=input("enter your file path")
    folder=ingest(folder_path)
    echunk=embed(folder)
    schunk=retrieve(echunk,q)
    answer=generate(schunk,q)
    claim=verify(schunk,answer)
    return claim

if __name__=="__main__":
    result = main()
    print(result)