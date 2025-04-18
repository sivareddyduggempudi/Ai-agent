import streamlit as st
from web_agent import ask_agent  

st.title("🔎 AI Web Browsing Agent (with Citations)")

query = st.text_input("Enter your question:")

if st.button("Search"):
    with st.spinner("🔍 Browsing the web and generating answer..."):
        result = ask_agent(query)
        st.markdown("### ✅ Answer (with Sources)")
        st.markdown(result, unsafe_allow_html=True)  
