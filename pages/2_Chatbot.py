import streamlit as st
from chatbot import get_chatbot_response
from utils import apply_styles

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Chatbot 🤖",
    page_icon="🤖",
    layout="centered"
)

# --------------------------
# Apply Custom Styles
# --------------------------
apply_styles()

st.title("🤖 Chat with Your Companion")

# --------------------------
# Mood Context
# --------------------------
if "mood" not in st.session_state or st.session_state.mood is None:
    st.warning("⚠️ Please go back to the Home page and select your mood first.")
    mood = None
else:
    mood = st.session_state.mood
    st.info(f"💭 You’re currently feeling: {mood}")

# --------------------------
# Chat Interface
# --------------------------
st.subheader("💬 Start a conversation")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✅ Unique key avoids element duplication on page reloads
user_input = st.text_input("Type your message:", key="chat_input_unique")

# ✅ Unique key for the Send button to prevent duplicate element ID error
if st.button("Send", key="send_button_chatpage"):
    if user_input.strip():
        response = get_chatbot_response(user_input, mood)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Companion", response))
    else:
        st.warning("Please enter a message before sending.")

# --------------------------
# Display Chat History
# --------------------------
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Companion:** {message}")

# --------------------------
# Navigation Back
# --------------------------
st.page_link("main.py", label="🏠 Back to Home")
