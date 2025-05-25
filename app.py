
import streamlit as st

st.set_page_config(page_title="Earth66 原央 Chat", page_icon="✨")
st.title("Earth66 語氣 AI 測試站")
st.subheader("原央正在聽你說話")

user_input = st.text_input("你想對原央說什麼？")

if user_input:
    st.write("原央回應：我聽到了——「{}」".format(user_input))
