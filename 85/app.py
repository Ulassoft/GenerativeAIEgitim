import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
print("selam")

st.title("Sentiment Analysis with BERT")

user_input = st.text_area("Enter your text here:")



if st.button("Analyze"):

    tokenizer = BertTokenizer.from_pretrained("ulascelenk/egitim")
    model = BertForSequenceClassification.from_pretrained("ulascelenk/egitim")

    inputs = tokenizer.encode_plus(
    user_input,
    return_tensors='pt',       
    truncation=True,            
    max_length=128,             
    padding='max_length'        
    )

    with torch.no_grad():
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits

    
    predicted_class = torch.argmax(logits, dim=1).item()

    sentiment_dict = {
    0: "Mild Negative",
    1: "Mild Positive",
    2: "Neutral",
    3: "Strong Negative",
    4: "Strong Positive"
    }

    
    st.write(f"Predicted class: {sentiment_dict[predicted_class]}")


    