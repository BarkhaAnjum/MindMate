import streamlit as st
from utils import get_fun_activity, apply_styles

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Fun Activity 🎉",
    page_icon="🎉",
    layout="centered"
)

# --------------------------
# Apply Custom Styles
# --------------------------
apply_styles()

st.title("🎉 Fun Activity to Brighten Your Day")

# --------------------------
# Mood Context
# --------------------------
if "mood" not in st.session_state or st.session_state.mood is None:
    st.warning("⚠️ Please go back to the Home page and select your mood first.")
else:
    st.info(f"💭 You’re currently feeling: {st.session_state.mood}")

# --------------------------
# Activity Suggestion
# --------------------------
if "fun_activity" not in st.session_state:
    st.session_state.fun_activity = get_fun_activity()

if st.button("✨ Give me a fun activity"):
    st.session_state.fun_activity = get_fun_activity()

st.success(st.session_state.fun_activity)

# --------------------------
# Navigation Back
# --------------------------
st.page_link("main.py", label="🏠 Back to Home")
