import json

def create_json(j, file_name: str) -> None:
    
    with open(f"{file_name}.json", "w") as outfile:
        json.dump(j, outfile)
        print(f"File {file_name} created")