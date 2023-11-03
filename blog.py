import json
import streamlit as st
import requests 
from PIL import Image
from streamlit_lottie import st_lottie

def load_url(url):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    else:
        return r.json()

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
            gaurav_url ="https://lottie.host/8e67d7e8-d8a9-450b-805f-b75f1bf60b23/0dCgmhG5us.json"
            coder = load_url(gaurav_url)
            st_lottie(coder, height=350, key="coder")

def scope():
    with st.container():
         st.header("Scope")
         left, right = st.columns(2)
         with left:
              laptop_url = "https://lottie.host/a9925a70-697b-4065-8962-dfcbdcd853c5/PFAvyqffOl.json"
              laptop = load_url(laptop_url)
              st_lottie(laptop, height=400, key="laptop")

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


def diagram():
    with st.container():
            st.write("---")
            st.header("How it works")
            st.write("This is a diagram showing how the project works ")
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
                

def works():
    st.header("Processing")
    st.write('''
        As you login and upload your PDFs and click on the process button:
        - All the text in the PDF is extracted.
        - All the text is divided into chunks.
        - All the chunks are turned into embeddings and stored in a vector database (e.g., FAISS).
        - All the embeddings are stored in a vector database (e.g., FAISS).
        ''')

def talk():
    with st.container():
        st.header("Now you are ready to chat")
        left, right = st.columns(2)
        with left:
            st.write('''
                    When you type in your question:
                    - Your question is embedded.
                    - We perform a similarity search in our vector DB.
                    - We rank the results we get.
                    - We send the best-ranked result and the question as the context to our LLM.
                    - We get the answer from the LLM.
''')
        with right:
            serch_url ="https://lottie.host/40e5e317-5032-455c-b024-7bd34465c1af/x5GpAiWxab.json"
            serch = load_url(serch_url)
            st_lottie(serch, height=300, key="serch")

def Bibliography():
    st.write("---")
    st.header("Bibliography")
    st.write("Webiste refrences")
    st.markdown("[Streamlit Doc ](https://docs.streamlit.io/)")
    st.markdown("[FAISS](https://ai.meta.com/tools/faiss/#:~:text=FAISS%20%28Facebook%20AI%20Similarity%20Search%2C%20more%20scalable%20similarity%20search%20functions.%29)")
    st.markdown("[LangChain](https://docs.langchain.com/docs/)")



