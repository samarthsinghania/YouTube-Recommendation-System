import json as js
d ={'a': [1,0,1] ,'b': [0,0,1], 'c': [1,0,1],'d': [1,1,0],'e': [0,0,0],'g': [1,0,1]}
with open("vector.json", "w") as f:
    js.dump(d,f)

from main import main_control as m

test_vector = [1,1,1]
obj = m()

print(obj.cosine_similar_top_n('g',4))

# l = [1,4,2]
# print(sorted(l,reverse=True))