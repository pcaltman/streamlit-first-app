import streamlit as st

st.title("Mon projet 1")

if st.session_state:
    st.write("Tu as :", st.session_state["age"])