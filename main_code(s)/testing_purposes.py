import json as js
from file_functions import Fily

# with open('main_code(s)/Json_files/video_words.json', 'w') as f:
#     w = js.dump({},f)

# # print(len(w)

obj = Fily()

# obj.video_all_words_gen()

# obj.bad_words_deleter()


with open('main_code(s)/Json_files/video_words.json', 'r') as f:
    w = js.load(f)
print(len(w))