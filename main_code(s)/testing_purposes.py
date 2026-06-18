from file_functions import Fily
from core_functions import main_control as m
import ijson as ij
import time
import numpy as np
# import random

fily = Fily()

# # # obj.cache_updater(['vid', ['v1', 'v2']])

core = m()

# # print(ob.random_vid_id_sender(4))

# # fily.cache_updater(['f',["id1", "id2", "id3", "id4", "id5", "id5"]])
# # print(core.random_vid_id_sender(4))
# print('hi')
# # print(core.update_vid_recommender('n_JwzBSsrnc'))
# # print(core.cosine_similar_top_n('n_JwzBSsrnc',3))

print(core.reset_homepage_to_random())

# given_vector_id = "naNcmnKskUE"
# quantity= 5

# start = time.time()
# print(core.reset_homepage_to_random())
# # print(core.cosine_similar_top_n(given_vector_id,5))

# # with open("main_code(s)/json_files/vector.json", "r") as f: #vectorjso contains
# #     for key,given_vector in ij.kvitems(f,''):
# #          if key == given_vector_id:
# #               break
    
            
# #     #its(vidinfo) in form: d ={'vidid': vector,..}
        


# #     # given_vector = vidinfo[given_vector_id]
# # with open("main_code(s)/json_files/vector.json", "r") as f: 
# #     cosine_list = []
# #     for vidid,vector in ij.kvitems(f,''):
# #         if given_vector_id==vidid: #ignore if given is there
# #             pass
# #         else:
# #                 # vector = vidinfo[vidid]
# #                 a_mag = np.linalg.norm(given_vector) #magnitudes 
# #                 b_mag = np.linalg.norm(vector)

# #                 dot = np.dot(given_vector,vector) #dot product
    
# #                 cosine_similar = dot/(a_mag*b_mag) #costheta
# #                 cosine_list.append((vidid, cosine_similar)) #appending to list
# #         #format: [(vidid, cosine_similar),...]

# #         #sorting on basis of 2nd element
# #     sorted_cosine_list = sorted(cosine_list,key=lambda x:x[1],reverse=True)
# #     topn=[]
# #     for i in range(0,quantity):
# #         topn.append(sorted_cosine_list[i][0])


# # print(topn)
# print("Total time: ", time.time()-start)

# vid_data =  [[1,2,3],[4,5,6]]
# L = [{
#         "id": vid_data[n][0],
#         "title": vid_data[n][1],
#         "channel": "StatQuest",
#         "img": vid_data[n][2]
#     } for n in range(len(vid_data))]
# print(L)

