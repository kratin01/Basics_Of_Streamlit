
import streamlit as st

# Set the title of the app
st.title("My First Streamlit App")
# Add a header
st.header("Welcome to Streamlit!")
# Add a subheader
st.subheader("This is a subheader")
# Add a text
st.text("This is a text")
# Add a Write
st.write("This is a write")
# Add a selectbox
lang=st.selectbox("Select Your Favorite Programming Language",["Python","Java","C++","JavaScript"])
# Add a radio
# st.radio("Select Your Favorite Programming Language",["Python","Java","C++","JavaScript"])
st.write(f"Ohh Wow! You selected {lang} as your favorite programming language")
# Success message
st.success(f"Congratulations! We will halp you learn {lang} programming language")