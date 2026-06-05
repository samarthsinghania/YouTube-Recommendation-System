# # import json as js
# # l = list({1,2,3,4})
# # with open('vectorformat.json','w') as f:
# #     js.dump(l,f)
# import numpy as np

# from file_functions import Fily

# # v = np.zeros(5,dtype=np.int8)
# # v[3]=1

# # print(v.tolist())

# #test:
# obj = Fily()

# # s = {'pizza', 'pineapple','ketchup',"mayo","newyork"}
# # word = ['pineapple', 'mayo']
# # print(s)
# # print(obj.vector_creator(word,s))

import numpy as np
import json as js
from main import main_control

obj = main_control()

v = np.array([[0,0,0,1,0,1,0,1,1,0],[0,1,0,1,1,0,0,1,1,0],[1,1,0,1,0,1,1,0,1,0]])
t = np.array([0,0,0,1,0,1,0,1,1,0])

# a_mag = np.linalg.norm(v)
# b_mag = np.linalg.norm(t)

given  = obj.cosine_similar(t,v)
for i in given:
    print(i)

print("hi",given[2])
