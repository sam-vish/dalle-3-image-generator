from openai import OpenAI
import os
from PIL import Image
import streamlit as st
from streamlit_carousel import carousel
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
openai_api_key = os.environ['OPENAI_API_KEY']

#initialize your image generation client
client = OpenAI(api_key=openai_api_key)

single_img = dict(
        title = "",
        text="",
        interval=None,
        img=" ",
    )
def generate_images(image_description, num_images):
    
    image_gallery = []
    for i in range(num_images):
        img_response = client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size= "1024x1024",
            quality= "standard",
            n=1
        )
        image_url = img_response.data[0].url
        # images.append(image_url)
        new_image = single_img.copy()
        new_image["title"] = f"Image {i+1}"
        new_image["text"] = image_description
        new_image["img"] = image_url
        image_gallery.append(new_image)
    return image_gallery
        
st.set_page_config(page_title="Dall-e Image Generator", page_icon=":camera:", layout="wide")

#create a title and a sub-title
st.title("DALL-E 3 Image Generator")
st.subheader("Powered by the world's most powerful Image generation API")

#text input
img_description = st.text_input("Enter a description of the image.")
num_of_images = st.number_input("Number of images to generate", min_value=1, max_value=5, value=1)

#create a button
if st.button("Generate Image"):
    generate_image = generate_images(img_description, num_of_images)
    
    carousel(items = generate_image, width =1)