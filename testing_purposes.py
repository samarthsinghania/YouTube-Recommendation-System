# import json as js
# d ={'cache':[0,0,0,0,0,0],'vids':[f'id{i}' for i in range(1,13) ]}
# with open("vid_detail_streamlit.json", "w") as f:
#     js.dump(d,f)

from file_functions import Fily

obj = Fily()

print(obj.vids_streamlit_updater([1,2,3,4,5,6]))