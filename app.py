import streamlit as st
from auth import *
from blog import *
from google.oauth2 import id_token
from google.auth.transport import requests
from user_handaling import *
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from HMLTemplats import css, bot_template, user_template


def get_pdf_text(pdf_doc):
    text = ""
    for pdf in pdf_doc:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="chat with pdf", page_icon=":books:", layout="wide",)
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    cookie_manager = stx.CookieManager()
    cookie_value = cookie_manager.get("username")

    with st.sidebar:
        if cookie_value is not None:
            if st.button("logout"):
                logout()
            st.write("Welcome", cookie_value)

        selected = option_menu(
            menu_title="Inquire.AI",
            options=["Chat", "login/signup", "Learn more", "Contact", "History"],
            icons=["chat-left-fill", "person-lines-fill",
                   "arrow-up-right-square", "bi bi-telephone", "clock-history"],
            menu_icon="Home",
            default_index=0
        )

    if selected == "Chat":
        st.subheader("upload your notes PDF 📄")
        pdf_doc = st.file_uploader("up-lode", accept_multiple_files=True)
        if st.button("process"):
            if cookie_value is not None:
                with st.spinner("processing"):
                    # get pdf text
                    raw_text = get_pdf_text(pdf_doc)
                    # st.write(raw_text)
                    # get text chunks
                    text_chunks = get_text_chunks(raw_text)
                    # st.write(text_chunks)
                    # create embeddings
                    vectorstore = get_vectorstore(text_chunks)
                    # create conversation chain
                    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

                    st.session_state.conversation = get_conversation_chain(vectorstore)
            else:
                st.warning("Please login")
        if cookie_value is not None:
            user_question = st.text_input("Ask inquireAI ")
            if user_question:
                handle_userinput(user_question)
    if selected == "login/signup":
        with st.container():
            st.subheader("login")
            username = st.text_input("Enter your email")
            password = st.text_input("password", type="password")
            if st.button("login"):
                login(username, password)
            st.write("---")
        with st.container():
            name = st.text_input("chose your name")
            email = st.text_input("email")
            nwe_password = st.text_input("code", type="password")
            if st.button("signup"):
                signup(name, nwe_password, email)

    if selected == "Learn more":
                greating()
                scope()
                works()

    if selected == "Contact":
        st.write("this is contact form")

    if selected == "History":
        st.subheader("Check  history")


if __name__ == '__main__':
    main()
