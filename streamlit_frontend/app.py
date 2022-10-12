import streamlit as st
import requests


st.title('PEPE Semantics')

text = st.text_input("Input text", "Hello")

button = st.button("Show me gifs!")

def predict(text):
    r = requests.post("https://pepe-semantics-w7jf4plb2a-uc.a.run.app/predict", json = {"text": text})
    dic = r.json()
    links = eval(dic['result'])
    top3 = links[:3]
    return top3

if button:
    top3 = predict(text)
    st.markdown("![Alt Text](" + top3[0] + ")")
    st.markdown("![Alt Text](" + top3[1] + ")")
    st.markdown("![Alt Text](" + top3[2] + ")")
    