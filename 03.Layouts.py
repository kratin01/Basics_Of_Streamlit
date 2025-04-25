# 03Layouts.py

import streamlit as st

# Title of the app
st.title("🎨 Learning Streamlit Layouts")

# Introduction
st.write("""
Welcome to the **Layouts & UI Demo**!  
This mini app will show how to use **columns**, **sidebars**, **markdown**, and **expanders** in Streamlit.
Feel free to click around and explore how interactive components work.
""")

# Create 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("❄️ Winter Season")
    st.image("https://images.pexels.com/photos/688660/pexels-photo-688660.jpeg?auto=compress&cs=tinysrgb&w=600", width=250)
    vote3 = st.button("Vote Winter")
    if vote3:
        st.success("Thank you for voting for **Winter season!**")

with col2:
    st.header("☀️ Summer Season")
    st.image("https://images.pexels.com/photos/189848/pexels-photo-189848.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=250)
    vote2 = st.button("Vote Summer")
    if vote2:
        st.success("Thank you for voting for **Summer season!**")

with col3:
    st.header("🌧️ Rainy Season")
    st.image("https://images.pexels.com/photos/913807/pexels-photo-913807.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=250)
    vote1 = st.button("Vote Rainy")
    if vote1:
        st.success("Thank you for voting for **Rainy season!**")

# Sidebar section
st.sidebar.header("🍽️ Customize Your Meal")

food = st.sidebar.selectbox("Select your favorite food:", ["Pizza", "Burger", "Pasta"])
drink = st.sidebar.selectbox("Select your favorite drink:", ["Coke", "Pepsi", "Fanta"])
dessert = st.sidebar.selectbox("Select your favorite dessert:", ["Ice Cream", "Cake", "Brownie"])

if st.sidebar.button("Order Now"):
    st.sidebar.success(f"Yay! Your order: **{food}**, **{drink}**, and **{dessert}** is on the way 🍕🥤🍰")
    st.sidebar.image("https://images.pexels.com/photos/15384761/pexels-photo-15384761/free-photo-of-slice-of-cake-and-an-iced-drink.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=250)

# Markdown Demo
st.subheader("📝 Markdown Examples")

st.markdown("### ➤ Headings & Formatting")
st.markdown("> This is a quote block for highlighting tips or notes.")
st.markdown("**Bold text** is useful for emphasis.")
st.markdown("~~Strikethrough~~ can show changes.")
st.markdown("`Inline code` is handy for small snippets.")
st.markdown("""
```python
# Multiline code block
print("Hello, Streamlit!")
```
""")

