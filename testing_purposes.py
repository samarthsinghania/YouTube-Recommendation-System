from file_functions import Fily
import json as js

with open('file.json', 'r') as f:
    data = js.load(f)



# print(type(data))
obj = Fily()
new = obj.Raw_Data_To_Normal(data)
# print("***NEW DATA****: ",new)
print(obj.data_appender(new_data=new))
