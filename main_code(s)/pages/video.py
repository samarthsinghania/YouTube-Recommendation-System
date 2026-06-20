import streamlit as st
import json as js
from file_functions import Fily
from core_functions import main_control
import time
import ijson

#Object initialisation
fily = Fily()
core = main_control()


with open('json_files/queue_video.json','r') as f:
    que_dic = js.load(f)
vid_id = que_dic['first']

st.video(f"https://www.youtube.com/watch?v={vid_id}", autoplay=True)

#Video title logic:
with open('json_files/normal_data.json') as f:
    for key, value in ijson.kvitems(f, ""):
        if key==vid_id:
            vid_title = value[1] #value looks like: [thumbnail, title, description]

st.header(vid_title)


#updating the recommendation
if vid_id!=0:
    time_start = time.time()
    print(core.update_vid_recommender_with_latest_video(vid_id))
    vid_id = 0
    print(time.time()-time_start)

#Back button Logic
button = st.button("go back")

if button:
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    st.switch_page('app.py')