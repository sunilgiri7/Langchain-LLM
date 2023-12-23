from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyAhy4JS0TtniFGcyx9vrsiuTSCvbNNkJAw"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

##Function to load Gemeni pro model and get response
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#Initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input: ", key="input")
submit=st.button("Ask the question...")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)