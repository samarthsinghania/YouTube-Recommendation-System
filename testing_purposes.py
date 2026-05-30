from file_functions import Fily
import json

with open('file.json', 'r') as f:
    data = json.load(f)

# print(type(data))
obj = Fily()
print(obj.Raw_Data_To_Normal(data))