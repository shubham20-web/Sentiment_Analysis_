# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained SVC and vectorizer
model = joblib.load('linearSVC_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def predict_sentiment(text):
    X_vect = vectorizer.transform([text])
    pred = model.predict(X_vect)[0]
    return pred

st.title("Sentiment Analysis Deployment: LinearSVC Model")
user_input = st.text_area("Enter your review text:", "")

if st.button("Analyze"):
    if user_input.strip():
        prediction = predict_sentiment(user_input)
        st.write(f"Predicted Sentiment: **{prediction}**")
    else:
        st.write("Enter text to analyze.")
