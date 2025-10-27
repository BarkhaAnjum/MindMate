import streamlit as st
import ollama
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
# Safety filter
# --------------------------
blocked_keywords = [
    "suicide", "kill myself", "self-harm",
    "murder", "terrorism", "violence", "harm"
]

def is_safe_prompt(prompt: str) -> bool:
    """Check if the user prompt contains harmful or unsafe keywords."""
    lowered = prompt.lower()
    return not any(keyword in lowered for keyword in blocked_keywords)

# --------------------------
# Chatbot response
# --------------------------
def get_chatbot_response(user_input: str, mood: str = None) -> str:
    """
    Generate chatbot response using Ollama.
    Mood (if available) is added to context for a personalized reply.
    """
    if not is_safe_prompt(user_input):
        return "⚠️ I'm really concerned about your message. Please reach out to a trusted friend, family member, or a professional for help. You're not alone 💜"

    mood_context = f"The user is currently feeling {mood}. " if mood else ""

    try:
        response = ollama.chat(
            model="gemma3:4b",  # ✅ updated to your installed model
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a supportive, empathetic mental health companion. "
                        "Always respond kindly, in a friendly and encouraging tone. "
                        "Avoid giving medical advice. Keep responses short and warm."
                    ),
                },
                {
                    "role": "user",
                    "content": mood_context + user_input,
                },
            ],
        )
        return response["message"]["content"]

    except Exception as e:
        # ✅ Friendly, crash-safe error message
        return (
            "⚠️ Sorry, I couldn’t get a response right now. "
            "Please make sure Ollama is running and the model 'gemma3:4b' is loaded.\n\n"
            f"Error: {e}"
        )

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
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message:", key="chat_input")

if st.button("Send"):
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
