import streamlit as st

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="MindMate",
    page_icon="🌸",
    layout="centered"
)

# --------------------------
# Global CSS Styles
# --------------------------
st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background: linear-gradient(135deg, #c8f0c8, #a8e6a3);
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        color: #2e7d32;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #2e7d32;
        font-weight: 700;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #2e7d32;
        color: #ffffff;
        border-radius: 10px;
        border: none;
        padding: 0.6em 1.2em;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #d81b60;
        color: #ffffff;
        transform: scale(1.03);
    }

    /* Alerts */
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 10px;
        padding: 1em;
        font-weight: 500;
    }
    .stSuccess { background-color: #dcedc8; color: #33691e; }
    .stInfo { background-color: #c8e6c9; color: #1b5e20; }
    .stWarning { background-color: #fff8e1; color: #ff6f00; }
    .stError { background-color: #f8bbd0; color: #c2185b; }

    /* Inputs */
    .stTextInput input, .stTextArea textarea {
        border: 2px solid #2e7d32;
        border-radius: 8px;
        padding: 0.5em;
        background-color: #f1f8f6;
    }

    /* Radio buttons */
    .stRadio label { color: #2e7d32 !important; font-weight: 500; }

    /* Footer & captions */
    footer, .stCaption { color: #33691e !important; font-style: italic; }
    </style>
    """,
    unsafe_allow_html=True
)



# --------------------------
# Home Page Content
# --------------------------
st.title("🌸 MindMate")
st.write("Your mood, your move. MindMate makes the rest easy. 🌼")

# Mood Selection
moods = ["😔 Sad", "😰 Anxious", "😡 Angry", "😊 Happy", "😩 Unmotivated", "😢 Lonely"]
if "mood" not in st.session_state:
    st.session_state.mood = None

st.subheader("💭 How are you feeling today?")
selected_mood = st.radio("Choose your mood:", moods, index=None, key="mood_selector")
if selected_mood:
    st.session_state.mood = selected_mood

# Navigation Buttons
st.subheader("✨ What would you like to do?")
col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/1_Affirmations.py", label="🌟 Affirmation")
with col2:
    st.page_link("pages/2_Chatbot.py", label="🤖 Chatbot")
with col3:
    st.page_link("pages/3_FunActivity.py", label="🎉 Fun Activity")

# Footer
st.markdown("---")
st.caption("Made with 💜 to support your mental well-being")
