#04DataHandling.py

import streamlit as st
import pandas as pd

st.title("🍕 Data Handling in Streamlit")
st.markdown("## 📊 Pizza Sales Dashboard")

file = st.file_uploader("📁 Upload your CSV file", type=["csv"])
if file:
    st.markdown("#### 👀 Data Preview")
    df = pd.read_csv(file)
    st.dataframe(df)

if file:
    if st.button("📈 Summary Statistics"):
        st.markdown("#### 📊 Summary Statistics")
        st.write(df.describe())

if file:
    st.markdown("#### 🔍 Filter Data")

    size = df["Size"].unique()
    selected_size = st.selectbox("🍕 Select the size of pizza", size)
    filtered_data = df[df["Size"] == selected_size]
    st.dataframe(filtered_data)
