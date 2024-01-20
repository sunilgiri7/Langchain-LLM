import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from PyPDF2 import PdfReader
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def pdf_to_text(uploadedFile):
    reader = PdfReader(uploadedFile)
    text = ""
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text += page.extract_text()
    return text


input_prompt = """
Evaluate the candidate's resume for a position in the technology field, focusing on software engineering, data science, data analysis, data engineering, big data engineering, and Python development. 
As a seasoned Application Tracking System (ATS), your goal is to provide a detailed analysis considering the competitive job market. 
Assign a percentage match based on the given job description and identify missing keywords with high accuracy.

Resume:
{text}

Job Description:
{jd}

Provide a response in the following format:
{{"JD Match": "%", "Missing Keywords": [], "Profile Summary": ""}}
"""



st.title("SMART ATS SYSTEM")
st.text("Improve Your Resume By Using Most Advanced ATS System")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="please upload the PDF")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = pdf_to_text(uploaded_file)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
        st.subheader(response)

