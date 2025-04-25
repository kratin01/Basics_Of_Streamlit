#05WebRequest.py

import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Live Currency Converter", page_icon="💱")

st.title("💱 Live Currency Converter")
st.markdown("## 🌍 Convert your currency to any other currency in the world")

# Amount input
amt = st.number_input("💰 Enter the amount you want to convert", min_value=1.0)

# Base and target currencies selection
base_url = "https://api.exchangerate-api.com/v4/latest/USD"
res = requests.get(base_url)

if res.status_code == 200:
    data = res.json()
    currencies = list(data["rates"].keys())

    col1, col2, col3 = st.columns([1, 0.2, 1])
    with col1:
        base_currency = st.selectbox("From Currency", currencies, index=currencies.index("INR"))
    with col2:
        st.markdown("### 🔁")
    with col3:
        target_currency = st.selectbox("To Currency", currencies, index=currencies.index("USD"))

    if st.button("Convert 💸"):
        conversion_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(conversion_url)

        if response.status_code == 200:
            conversion_data = response.json()
            rate = conversion_data["rates"].get(target_currency)

            if rate:
                converted_amt = amt * rate
                last_updated = datetime.fromtimestamp(conversion_data['time_last_updated']).strftime("%Y-%m-%d %H:%M:%S")

                st.success(f"✅ {amt:.2f} {base_currency} = {converted_amt:.2f} {target_currency}")
                st.info(f"💹 Exchange Rate: 1 {base_currency} = {rate:.4f} {target_currency}")
                st.caption(f"🕒 Last Updated: {last_updated}")
            else:
                st.error("❌ Target currency not found.")
        else:
            st.error("❌ Error fetching conversion rate. Please try again later.")
else:
    st.error("❌ Error loading currency list. Check your connection.")
