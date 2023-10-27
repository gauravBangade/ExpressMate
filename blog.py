import json
import streamlit as st
import requests 
from PIL import Image

def greating():
    with st.container():
        st.subheader("Hi, I am Gaurav :wave:")
        left, right = st.columns(2)
        with left:
            st.title("I am a second year student MCA student")
            st.write("##")
            st.write( 
                """
                    This page will be the full introduction to my sem III project inquireAI 
                    - Scoop and goal of this project 
                    - How this site works 
                    - Designe & Diagrams and Architecture
                    - Bibliography 
                """)
            st.write("---")
        
        with right:
            st.text_area("lotte file ")

def scope():
    with st.container():
         st.header("Scope")
         left, right = st.columns(2)
         with left:
             st.write("laptop")
         with right:
            st.write("##")
            st.write(
             ''' 
               
                The primary goal of this website is to facilitate natural language interactions with your own documents. 
                This platform allows you to effortlessly upload your documents or PDFs and query them with efficiency.
                Unlike many modern AI chatbots, such as ChatGPT, which often struggle with grasping the context of your
                questions or lack specific information due to context limitations, our tool is designed to address these 
                issues. For instance, students can upload all their notes and effortlessly query the AI for any information, 
                making the study process faster and more convenient.

                Another valuable way to utilize this tool is by uploading your entire documentation, 
                enabling you to gain a deeper understanding of its contents. 
                This website serves as a versatile solution for engaging with your documents in a more conversational 
                and effective manner, enhancing your ability to extract insights and information from them.
            '''
            )


def works():
    with st.container():
            st.write("---")
            st.header("How it works")
            st.write("This is how the core funcanality of the project works ")
            image, text = st.columns((2, 1))
            with image:
                Diagram = Image.open("images\Diagrams.png")
                st.image(Diagram)
        
            with text:
                st.header("Tech stack ")
                st.write("##")
                st.write(
                '''
                 Technology's used 
                 - Python
                 - streamlit 
                 - mongoDB
                 - langchain
                 - FAISS
                 - hosting git etc 
                       ''')
    st.write("ivnof")


