import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch


st.title("Sentiment Analysis with BERT")

user_input = st.text_area("Enter your text here:")



if st.button("Analyze"):  
    st.write(user_input)


    