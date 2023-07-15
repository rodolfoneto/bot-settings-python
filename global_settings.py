from pathlib import Path
import json

def save(obj):
    file_path = "settings.json"
    if Path(file_path).exists() == False or Path(file_path).is_file() == False:
        raise Exception("save(): Arquivo setting com problema")
    file = open('settings.json', 'w')
    json.dump(obj, file, sort_keys=True, indent=4)
    file.close()

def load():
    file_path = "settings.json"
    if Path(file_path).exists() == False or Path(file_path).is_file() == False:
        raise Exception("load(): Arquivo setting com problema")
    
    with open(file_path, 'r') as file:
        setting = json.load(file)
    return setting

def get(item):
    obj = load()
    return obj[item]