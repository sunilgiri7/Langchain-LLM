from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Gemini Pro Vision

def get_gemeni_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytedata = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytedata
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file is uploaded")

# Initialize Streamlit
st.set_page_config(page_title="Multilanguage Invoice Extractor")
st.header("Gemini Application")
input = st.text_input("Input Prompt:", key="input")
upload_file = st.file_uploader("Choose an image of invoice...", type=["jpg","jpeg","png"])

image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded invoice", use_column_width=True)

submit = st.button("Tell me about the invoice")
input_prompt = '''
                you are an expert in understanding invoices. we will upload a image as invoices and you will
                have to answer any questions based on the uploaded invoice image
'''
if submit:
    image_data = input_image_setup(upload_file)
    response = get_gemeni_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)
