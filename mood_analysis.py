import streamlit as st
from textblob import TextBlob
from utils import apply_styles

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Mood Analysis 🌈",
    page_icon="🌈",
    layout="centered"
)

# --------------------------
# Apply Custom Styles
# --------------------------
apply_styles()

st.title("🌈 Mood Analysis")

# --------------------------
# Mood Input
# --------------------------
user_input = st.text_area("💬 Share how you’re feeling right now:")

if st.button("🔎 Analyze Mood"):
    if user_input.strip():
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Classify mood based on polarity
        if polarity > 0.3:
            mood = "happy"
        elif polarity < -0.3:
            mood = "sad"
        else:
            mood = "neutral"

        st.session_state.mood = mood

        st.success(f"✅ Analysis complete! Your mood seems to be **{mood.capitalize()}** 🌟")
    else:
        st.warning("⚠️ Please enter some text before analyzing.")

# --------------------------
# Navigation Back
# --------------------------
st.page_link("main.py", label="🏠 Back to Home")
