import streamlit as st
from datetime import date

# adding image

st.image("https://media.istockphoto.com/id/1442417585/photo/person-getting-a-piece-of-cheesy-pepperoni-pizza.jpg?s=612x612&w=0&k=20&c=k60TjxKIOIxJpd4F4yLMVjsniB4W1BpEV4Mi_nb4uJU=")
st.title("Pizza Order App🍕")

name = st.text_input("Enter Your Name")
DOB=st.date_input("Enter Your Date of Birth")

if st.button("Save Details"):
    st.success(f"Details Saved Successfully!")
    st.write(f"Hey {name}, we are happy to serving pizza to a person who is {date.today().year - DOB.year} years old")

    st.balloons()

category = st.selectbox("Select Your Favorite Pizza Category", ["Veg", "Non-Veg"])
if category=="Veg":
    pizza = st.selectbox("Select the pizza you want", ["Margherita", "Farmhouse", "Peppy Paneer"])
    if pizza:
        slider=st.select_slider("Select the size of pizza", options=["Small", "Medium", "Large"])
        if st.button("Order Now"):
            st.success(f"Hey {name}, your {category} {pizza} pizza of size {slider} will be delivered to you in 30 minutes")
else:
    pizza = st.selectbox("Select the pizza you want", ["Chicken Tandoori", "Chicken BBQ", "Chicken Supreme"])
    if pizza:
        slider=st.select_slider("Select the size of pizza", options=["Small", "Medium", "Large"])
        if st.button("Order Now"):
            st.success(f"Hey {name}, your {category}  {pizza} pizza of size {slider} will be delivered to you in 30 minutes")

# Rate the app
st.subheader("Rate the Pizza Order App⭐")
rating = st.slider("Select a rating", 1, 5, 3)
if st.button("Submit Rating"):
    # st.success(f"Thank you for rating the app {rating} out of 5")
    if rating<3:
        st.warning("We will try to improve the app")
    else:
        st.balloons()
        st.success("Thank you for your positive feedback!")