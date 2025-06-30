
import streamlit as st
from textblob import TextBlob

# --- App Styling ---
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💬 Sentiment Analysis App</h1>", unsafe_allow_html=True)
st.markdown("### Analyze the sentiment of a review or tweet in seconds!")

# --- Sidebar ---
with st.sidebar:
    st.markdown("## 📘 About")
    st.write("This app uses NLP to analyze if the entered text is Positive, Neutral, or Negative.")
    st.markdown("### ✨ Try Sample Text")
    if st.button("Try Positive"):
        st.session_state.text = "I absolutely love this product! Highly recommend."
    if st.button("Try Negative"):
        st.session_state.text = "Worst experience ever. Totally disappointed."
    if st.button("Try Neutral"):
        st.session_state.text = "The movie was okay. Nothing special."

# --- Input Text ---
text = st.text_area("📝 Enter your text here:", value=st.session_state.get("text", ""), height=150)

# --- Analyze Button ---
if st.button("🔍 Analyze Sentiment"):
    if text:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "Positive 😊"
            bg_color = "#D4EDDA"
        elif polarity < -0.1:
            sentiment = "Negative 😞"
            bg_color = "#F8D7DA"
        else:
            sentiment = "Neutral 😐"
            bg_color = "#FFF3CD"

        st.markdown(
            f"<div style='background-color: {bg_color}; padding: 20px; border-radius: 10px; text-align: center;'>"
            f"<h2>Sentiment: {sentiment}</h2>"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter some text!")

# --- Footer ---
st.markdown("<hr><center>Developed by Ansiya • Internship AI Project</center>", unsafe_allow_html=True)
