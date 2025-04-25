# 01Basic.py
import streamlit as st

# Set the title of the app
st.title("👋 Welcome to Your First Streamlit App")

# Header section
st.header("🚀 Let's Explore the Basics of Streamlit")

# Subheader section
st.subheader("📌 What is Streamlit?")
st.write("""
Streamlit is an open-source Python library that makes it easy to build and share beautiful, custom web apps for machine learning and data science.

With just a few lines of code, you can create interactive dashboards, tools, or data apps—without needing any front-end knowledge!
""")

# Add basic text elements
st.subheader("🧱 Basic Components")
st.text("🔹 st.text() - Used to show simple text.")
st.write("🔹 st.write() - More flexible. You can show text, numbers, dataframes, plots, etc.")

# Add an interactive selectbox
st.subheader("🎯 Select Your Favorite Programming Language")
lang = st.selectbox(
    "Choose a language you love coding in:",
    ["Python", "Java", "C++", "JavaScript"]
)

# Display result
st.write(f"👍 Awesome! You selected **{lang}** as your favorite language.")

# Display a success message
st.success(f"You're on the right path to mastering {lang}. Let's learn together! 💪")

# Add a tip at the end
st.info("Tip: Try editing this app and changing the widgets to see how Streamlit works!")
