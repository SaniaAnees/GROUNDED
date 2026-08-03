import pathlib

def ingest(folder_path):
    file=[]
    extensions=[".cmake",".h",".pc",".gitignore",".c",".md"]
    folder=pathlib.Path(folder_path)
    for files in [p for p in folder.rglob("*") if p.suffix.lower() in extensions]:
        try:
            file.append({"filename":files,"content":files.read_text()})
        except UnicodeDecodeError:
            print(f"Skipped {files.name} - encoding error")
            continue
        except Exception as e:
            print(f"Skipped {files.name} - {e}")
            continue
    return file
def main():
    folder=input("Enter the path for the folder : ")
    return ingest(folder)
if __name__=="__main__":
   result = main()
   print(f"Found {len(result)} files")
   for item in result:
       print(item["filename"])