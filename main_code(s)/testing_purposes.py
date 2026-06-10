import json as js
from file_functions import Fily

with open('main_code(s)/Json_files/normal_data.json', 'r') as f:
    w = js.load(f)

print(len(w))
