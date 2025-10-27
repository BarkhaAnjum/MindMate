import streamlit as st
from utils import get_affirmation, apply_styles

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Affirmations 🌟",
    page_icon="🌟",
    layout="centered"
)

# --------------------------
# Apply Custom Styles
# --------------------------
apply_styles()

st.title("🌟 Your Personalized Affirmation")

# --------------------------
# Mood Check
# --------------------------
if "mood" not in st.session_state or st.session_state.mood is None:
    st.warning("⚠️ Please go back to the Home page and select your mood first.")
else:
    mood = st.session_state.mood
    affirmation = get_affirmation(mood)

    st.subheader(f"💭 You mentioned feeling {mood}")
    st.success(affirmation)

# --------------------------
# Navigation Back
# --------------------------
st.page_link("main.py", label="🏠 Back to Home")
