import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load environment variables securely
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Function to fetch response from Gemini model, handling potential errors
def get_gemini_response(input1, image):
    model = genai.GenerativeModel("gemini-pro-vision")
    try:
        if input1 != "":
            response = model.generate_content([input1, image])
        else:
            response = model.generate_content(image)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while generating response: {e}")
        return "Unable to process request at this time. Please try again later."

# Layout and styling
st.set_page_config(page_title="Gemini Image Insights", layout="wide")  # Wider layout
st.title("Unlock Image Insights with Gemini")  # Compelling title

# Input section
st.subheader("Tell me about your image:")
input1 = st.text_input("Provide a descriptive prompt (optional):", key="input")
uploaded_file = st.file_uploader("Upload an image", type=["jpeg", "jpg", "png"], accept_multiple_files=False)

# Image preview and analysis
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Insights"):
        response = get_gemini_response(input1, image)
        st.markdown(f"**<br>Gemini's Insights:**<br>{response}", unsafe_allow_html=True)  # Enhanced formatting

# Footer
st.markdown(
    """
---
**Created with  by Bard**
""",
    unsafe_allow_html=True,
)  # Footer with a personal touch
