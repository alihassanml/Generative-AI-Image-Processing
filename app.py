import streamlit as st
import PIL.Image
import google.generativeai as genai
from gtts import gTTS
import os
import tempfile

api_key = 'AIzaSyBpKg-qIxLoHVJ2KACeuF4inH1SatDl_Bw'

genai.configure(api_key=api_key)

def Image_Processing(prompt, image_path):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([prompt, image_path])
    return response.text

def main():
    st.title('LangChain Image Processing Model')
    user_input = 'Please describe the contents of the uploaded image in detail. Mention key objects, actions, people, and any relevant context.'
    image = st.file_uploader('Upload File', type=['jpg', 'png', 'jpeg'])
    if image:
        user_image = PIL.Image.open(image)
        
        response = Image_Processing(user_input, user_image)
        
        st.write(response)

main()
