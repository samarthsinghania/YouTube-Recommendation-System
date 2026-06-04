# import json as js
# l = list({1,2,3,4})
# with open('vectorformat.json','w') as f:
#     js.dump(l,f)
import numpy as np

from file_functions import Fily

# v = np.zeros(5,dtype=np.int8)
# v[3]=1

# print(v.tolist())

#test:
obj = Fily()

s = {'pizza', 'pineapple','ketchup',"mayo","newyork"}
word = ['pineapple', 'mayo']
print(s)
print(obj.vector_creator(word,s))

