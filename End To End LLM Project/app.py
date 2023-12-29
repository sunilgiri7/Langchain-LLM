import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#function to get response from Llma 2
st.set_page_config(page_title="Generate Blogs",
                   page_icon="LLM",
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Generate Blogs LLM")
input_text = st.text_input("Enter the blog topic!")


## creating two more columns for additional 2 fields
col1, col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("No of words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientist", "Common Peoples"), index=0)

submit = st.button("Generate")

def get_llama_response(input_text, no_words, blog_style):
    ## Llama model
    llm = CTransformers(model = "model/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    template = '''
                write a blog for {blog_style} 
                job profile for a topic {input_text} 
                within {no_words} words.
                '''
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)
    
    ##Generate response
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response

# final response
if submit:
    st.write(get_llama_response(input_text, no_words, blog_style))
