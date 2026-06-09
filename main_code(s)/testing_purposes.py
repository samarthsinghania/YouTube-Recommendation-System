# import json as js
# d ={'cache':[0,0,0,0,0,0],'vids':[f'id{i}' for i in range(1,13) ]}
# with open("vid_detail_streamlit.json", "w") as f:
#     js.dump(d,f)

from file_functions import Fily

obj = Fily()

print(obj.word_extractor(['hello HEyyy+MROW LK^#$SHARMA@#SIRR my name is# /samarth singhania', 'hi ho'], lower=True))
# print(obj.vids_streamlit_updater([1,2,3,4,5,"meowj"]))
# print(obj.cache_updater('id8'))