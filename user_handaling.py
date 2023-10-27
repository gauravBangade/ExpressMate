import streamlit as st
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
import re
import extra_streamlit_components as stx

cookie_manager = stx.CookieManager()
client = MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
users = db["users"]


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def logout():
    cookie_manager.delete("username")


def login(email, password):
    user_data = users.find_one({"email": email})

    if user_data and pbkdf2_sha256.verify(password, user_data["password"]):
        uname = user_data["username"]
        cookie_manager.set("username", uname)
        st.success("Login successful! Welcome ")
        st.write("Welcome ", uname)
    else:
        st.error("Login failed. Please check your username and password.")
        st.write("try signing up below")


def signup(username, password, email):
    # Hash the password before storing it
    hashed_password = pbkdf2_sha256.hash(password)
    # email validation
    if is_valid_email(email):
        # Check if the username already exists
        if users.find_one({"email": email}):
            st.error("User with this email already exists. Please choose a different one.")
        else:
            user_data = {"username": username, "password": hashed_password, "email": email}
            users.insert_one(user_data)
            st.success("Signup successful! You can now log in.")
    else:
        st.warning("invalid email")
