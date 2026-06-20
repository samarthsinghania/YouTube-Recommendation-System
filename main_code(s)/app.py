import streamlit as st
import time 
import json as js
from st_clickable_images import clickable_images
from st_click_detector import click_detector
from file_functions import Fily
from core_functions import main_control
 
#Object initialisation
fily = Fily()
core = main_control()

#Page title 
st.set_page_config(page_title="YT RS", page_icon = 'resources/icon.png',layout="wide")


st.header('YouTube Recommendation System')



#for wide streamlit app


#for removing streamlit's watermark and the default menu option
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

#text
st.text('HELLO THIS IS AN APPs')

#sidebar
with st.sidebar:
    st.text("HEy Welcome to Youtube")
    st.image("https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700")


image_lis = [
        "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
        "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
        "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
        "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
        "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
    ]

image_lis2 = ["https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700"]
# clicked = clickable_images(
#     image_lis,
#     titles=[f"Image #{str(i)}" for i in range(5)], #[Image 0, Image 1..basically]
#     div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
#     img_style={"margin": "5px", "height": "200px"},
# )
# st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")



#here we gather video data:
with open('json_files/normal_data.json','r') as f:
    normal_data = js.load(f)


#here we gather video data:
with open('json_files/vid_detail_streamlit.json','r') as f:
    vid_detail = js.load(f)

all_vid = vid_detail['vids_streamlit'] #all videos in list

vid_data = []
for vid in all_vid:
    title = normal_data[vid][1]
    img = normal_data[vid][0]
    vid_data.append([vid,title,img])

#vid_data format:
# [[vid1],[vid2]...., [vid9]]
#for each vid-> [id,title,thumbnail_link]

videos = [
    {
        "id": vid_data[n][0],
        "title": vid_data[n][1],
        "channel": "StatQuest",
        "img": vid_data[n][2]
    }
    for n in range(12)]
#this is a list-comprehension 
cards = ""

for video in videos:

    cards += f"""
    <div style="width:350px;">
        <a href='#' id='{video["id"]}'>  
            <img
                src='{video["img"]}'
                style='width:100%; border-radius:12px;'
            >
        </a>

        <h4>{video["title"]}</h4>

    </div>
    """
content = f"""
<div style="
    display:flex; 
    flex-wrap:wrap;
    justify-content:center;
    gap:5px;
">
    {cards}
</div>
"""
#what each function does:
# display:flex;          /* video children go left-to-right */
# flex-wrap:wrap;        /* start a new row when needed */
# justify-content:center;/* center the rows */
# gap:50px;              /* spacing between cards */

clicked = click_detector(content) 

st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")

if clicked != '':
    #updating first queue
    # print(fily.update_queue(clicked,'1')) #this isnt working for some reason..
    with open('json_files/queue_video.json','w') as f:
        js.dump({'first':clicked},f)

    # core.update_vid_recommender_with_latest_video(clicked)

    #Changing the page
    st.switch_page('pages/video.py')

reset_button = st.button("Reset")

if reset_button:
    fily.update_queue(0,'1')
    core.reset_homepage_to_random()

    #Loading Bar Logic
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    st.rerun()