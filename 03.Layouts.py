import streamlit as st

st.title("Learing Streamlit Layouts🚀")


col1,col2,col3=st.columns(3)

with col1:
    st.header("Winter Season")
    st.image("https://images.pexels.com/photos/688660/pexels-photo-688660.jpeg?auto=compress&cs=tinysrgb&w=600",width=250)
    vote3=st.button("Vote Winter season")
    if vote3:
        st.success("Thank you for voting for **Winter season!❄️**")

with col2:
    st.header("Summer Season")
    st.image("https://images.pexels.com/photos/189848/pexels-photo-189848.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",width=250)
    vote2=st.button("Vote Summer season")
    if vote2:
        st.success("Thank you for voting for **Summer season!☀️**")
with col3:
    st.header("Rainy Season")
    st.image("https://images.pexels.com/photos/913807/pexels-photo-913807.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",width=250)
    vote1=st.button("Vote Rainy season")
    if vote1:
        st.success("Thank you for voting for **Rainy season!🌧️**")


# SiderBar

st.sidebar.header("This is a sidebar")

food=st.sidebar.selectbox("Select your favorite food",["Pizza","Burger","Pasta"])
drink=st.sidebar.selectbox("Select your favorite drink",["Coke","Pepsi","Fanta"])
dessert=st.sidebar.selectbox("Select your favorite dessert",["Ice Cream","Cake","Brownie"])
if st.sidebar.button("Order Now"):
    st.sidebar.write(f"We are happy to serve you **{food}** with **{drink}** and **{dessert}** as dessert👩🏻‍🍳")
    st.sidebar.image("https://images.pexels.com/photos/15384761/pexels-photo-15384761/free-photo-of-slice-of-cake-and-an-iced-drink.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",width=250)
    
    
    #MARKDOWNS
    
st.subheader("Markdowns")
st.markdown("# This is a Heading")
st.markdown("> this is a blockquote")
st.markdown("**This is a bold text**")
st.markdown("~~This is a strikethrough text~~")
st.markdown("`This is a code`")
st.markdown("```python\nprint('Hello World')\n```")

st.header("Expanders")

with st.expander("Recipe of Pizza"):
    st.write("1. Take a pizza base")
    st.write("2. Add sauce")
    st.write("3. Add toppings")
    st.write("4. Bake it in oven")
    st.write("5. Serve it hot")


