import json as js
from file_functions import Fily
from core_functions import main_control

# with open('main_code(s)/Json_files/video_words.json', 'w') as f:
#     w = js.dump({},f)

# # print(len(w)

obj = Fily()

# obj.video_all_words_gen()

# # obj.bad_words_deleter()


# with open('main_code(s)/Json_files/all_video_words.json', 'r') as f:
#     l = js.load(f)
# print(len(l))
# print(obj.all_vector_words_creator())

# L = ['Hi','meow','cat']
# # print(set(L))

# print((",".join(L)).lower().split(','))



#to convert everything to lower
# with open('main_code(s)/Json_files/video_words.json', 'r') as f:
#     dic = js.load(f)

# new_dic ={}
# for vid_id in dic:
#     lis = dic[vid_id]
#     new_lis = (",".join(lis)).lower().split(',')
#     new_dic[vid_id] = new_lis
# with open('main_code(s)/Json_files/video_words.json', 'w') as f:
#     js.dump(new_dic,f)

"Making vector.json"
# obj.all_videos_vector_json_maker()


"MAIN"

o = main_control()

import time

current_time=time.time()

print(o.cosine_similar_top_n('1etaZ5ITXlg',2))

print("time taken: ",time.time()-current_time)