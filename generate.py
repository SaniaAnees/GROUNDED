import ollama
from ingest import ingest
from embed import embed
from retrieve import retrieve
def generate(schunk,question):
    try:
        context="\n".join([file["content"] for file in schunk])
        prompt=f"You are a lead principal  architect of a top tech company. Answer the user query provide:\n {question}\nAlso refer to the context provided below..\n {context}"
        result=ollama.chat(model="mistral",messages=[{"role":"user","content":prompt}])
        answer = result['message']['content']
        return answer
    except ollama.ResponseError as e:
        print(f"Ollama API Error (Status {e.status_code}): {e.error}")
    except Exception as e:
        print(f"An unexpected connection or system error occurred: {e}")
def main():
    q=input("enter your question?")
    folder_path=input("enter your file path")
    folder=ingest(folder_path)
    echunk=embed(folder)
    schunk=retrieve(echunk,q)
    result=generate(schunk,q)
    return result
if __name__=="__main__":
    result=main()
    print(result)