import streamlit as st
from textblob import TextBlob
st.sidebar.title("about us")
st.sidebar.text("""Name:Pankaj Sajwan
Qualification:B.Tech in Mechanical Engineering
Currently Persuing Data Science Course from Ducat
""")

st.sidebar.title("contact us")
st.sidebar.text("""Email:pankaj.sajwan20@gmail.com
Mob No:+91 8477979148
""")

st.title("Sentiment Analysis project")

text=st.text_input("**enter text**")
btn=st.button("predict") 

if btn:
    blob=TextBlob(text)
    sent=blob.sentiment[0]
    if sent<0:
        st.error("Negative Sentiment")
        st.image("neg_senti.jpg")
    elif sent>0:
        st.success("Positive Sentiment")
        st.image("pos_senti.jpg")
    else:
        st.warning("Neutral Sentiment")
        st.image("neutral_senti.jpg")









        
