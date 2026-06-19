import streamlit as st
import json as js
from file_functions import Fily
from core_functions import main_control
 
#Object initialisation
fily = Fily()
core = main_control()


with open('json_files/queue_video.json','r') as f:
    que_dic = js.load(f)
vid_id = que_dic['first']

st.video(f"https://www.youtube.com/watch?v={vid_id}", autoplay=True)
st.text('hola yo soy dora')


#updating the recommendation
print(core.update_vid_recommender_with_latest_video(vid_id))


#Back button Logic
button = st.button("go back")

if button:
    st.switch_page('app.py')