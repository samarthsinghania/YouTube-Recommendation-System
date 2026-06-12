import streamlit as st
import time 
import json as js
from st_clickable_images import clickable_images

#Page title 
st.set_page_config(page_title="YT RS")
#icon
st.set_page_config(page_title="Surge Price Prediction App", page_icon = 'resources\icon.png')


st.header('YouTube Recommendation System')



#for wide streamlit app
st.set_page_config(layout="wide")

#*********

# image_lis = [
#         "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
#         "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
#         "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
#         "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
#         "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
#     ]
# clicked = clickable_images(
#     image_lis,
#     titles=[f"Image #{str(i)}" for i in range(5)], #[Image 0, Image 1..basically]
#     div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
#     img_style={"margin": "5px", "height": "200px"},
# )
# st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

