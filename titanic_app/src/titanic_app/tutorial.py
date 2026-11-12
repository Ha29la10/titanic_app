from idlelib import search

import streamlit as st

st.write("hello from titanic_app")
st.radio("select a number",[1,2,3],index=0)
checked= st.checkbox("check")
if checked:
    st.write("checked")
with st.form("search"):
    name=st.text_input("enter your name",placeholder="Allen")
    classes=st.multiselect("class",[1,2,3],default=[1,2,3])
    ages=st.slider("age",0,80,(0,80))
    submitted=st.form_submit_button("Search")
if submitted:
    st.write(f"search{name} in class{classes}and age{ages}")
