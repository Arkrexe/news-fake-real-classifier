import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

pipeline = joblib.load("news_pipeline.pkl")

def clean_text(text):
    text = str(text).lower()
    text = ''.join(c for c in text if c not in string.punctuation)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

st.title("📰 News Article Classifier")
st.subheader("Check if a news article is Real or Fake")

input_text = st.text_area("Paste a news article here:")

if st.button("Check"):
    cleaned = clean_text(input_text)
    result = pipeline.predict([cleaned])[0]
    output = "REAL" if result == 0 else "FAKE"
    st.success(f"✅ The news is predicted to be: **{output}**")