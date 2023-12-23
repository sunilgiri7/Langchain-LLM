from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

os.environ['GOOGLE_API_KEY'] = "AIzaSyAhy4JS0TtniFGcyx9vrsiuTSCvbNNkJAw"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


def get_gemini_response(input1, image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if input!= "":
        response = model.generate_content([input1, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input1 = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose a image...", type=['jpeg', 'jpg', 'png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='uploaded image', use_column_width=True)


submit = st.button("Tell me about the image")
if submit:
    response = get_gemini_response(input1, image)
    st.write(response)