import streamlit as st
import time 
import json as js
from st_clickable_images import clickable_images
from st_click_detector import click_detector

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

#tex
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

videos = [
    {
        "id": "vid1",
        "title": "Linear Regression Explained",
        "channel": "StatQuest",
        "img": image_lis[0]
    },
    {
        "id": "vid2",
        "title": "Neural Networks Amazing video man just watch it!",
        "channel": "The Young Technical Guy",
        "img": image_lis[1]
    },
    {
        "id": "vid3",
        "title": "Neural Networks",
        "channel": "3Blue1Brown",
        "img": image_lis[1]
    },
    {
        "id": "vid4",
        "title": "Neural Networks",
        "channel": "3Blue1Brown",
        "img": image_lis[1]
    },
    {
        "id": "vid5",
        "title": "Neural Networks",
        "channel": "3Blue1Brown",
        "img": image_lis[1]
    }
    # ...
]
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

        <p style='color:gray;'>
            {video["channel"]}
        </p>
    </div>
    """
content = f"""
<div style="
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:50px;
">
    {cards}
</div>
"""


clicked = click_detector(content)

st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")