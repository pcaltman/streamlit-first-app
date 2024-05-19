import streamlit as st

st.set_page_config(
    page_title="Multipage app",
    page_icon="♥️",
)

st.title("Main page")
st.sidebar.success("Select a page above")

if "age" not in st.session_state:
    st.session_state["age"]=""

var = st.text_input("Entre ton age", st.session_state["age"])
submit = st.button("Submit")

if submit:
    st.session_state["age"]= var
    st.write("Votre age est de", var)