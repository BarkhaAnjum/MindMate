import random
import streamlit as st

# --------------------------
# Affirmations Dictionary
# --------------------------
# Copy your affirmations dictionary here
affirmations = {
    "sad": [
        "It’s okay to feel sad — your feelings are valid. Healing begins when you give yourself permission to feel.",
        "Sadness does not mean weakness; it means something mattered to you deeply.",
        "You are not defined by this difficult moment — you are defined by your resilience.",
        "Even when skies are grey, the sun exists behind the clouds — so does your light.",
        "One day, this sadness will be a memory that proves your strength.",
        "Tears are healing, not shameful — they show the depth of your humanity.",
        "Your worth does not disappear when you feel low. It remains constant.",
        "Sadness is a chapter, not your whole story.",
        "You are allowed to grieve without rushing yourself back to happiness.",
        "You don’t need to fight sadness today — just sit with it gently.",
        "Even in your lowest moments, someone loves you and values your presence.",
        "This feeling will soften with time, even if it doesn’t feel like it now.",
        "Every step forward, even small, is proof that you’re moving through this.",
        "You can allow yourself to rest without guilt. Rest is healing.",
        "You are not broken — you are becoming whole in new ways."
    ],

    "anxious": [
        "Anxiety is not permanent — it’s a passing wave, and you have the strength to ride it.",
        "Your breath is an anchor; return to it when your mind feels stormy.",
        "You are not your anxious thoughts — you are the calm observer of them.",
        "Slow down. Nothing requires you to figure out everything all at once.",
        "You’ve survived every anxious moment so far — this one will pass, too.",
        "When your heart races, remind yourself: this is my body trying to protect me.",
        "It’s safe to pause and take a break from overthinking.",
        "You can choose not to engage every ‘what if.’ You are allowed to let thoughts float by.",
        "Even with anxiety, you are capable of living fully and meaningfully.",
        "Take today one small step at a time — that’s enough.",
        "Fear exaggerates, but you can respond with compassion.",
        "It’s okay to not have all the answers right now.",
        "Your nervous system can be soothed — try breathing slowly, in and out.",
        "Worry does not define you. Strength does.",
        "You are safe in this moment, right here and right now."
    ],

    "angry": [
        "Anger is a messenger — it often signals hurt or fear beneath the surface.",
        "You are not your anger; you are the wise part that can observe and guide it.",
        "It’s okay to pause before responding — that pause is power.",
        "Anger shows you care about something important — listen to it, then respond calmly.",
        "Releasing anger doesn’t mean you’re weak — it means you’re choosing peace.",
        "You can express yourself firmly without losing your calm.",
        "Breathing deeply is not avoidance; it’s reclaiming control.",
        "Your worth is not measured by your reaction — but by your reflection.",
        "You can let go of carrying this weight longer than needed.",
        "Sometimes the strongest action is walking away from conflict.",
        "You are allowed to be assertive without being destructive.",
        "Your voice matters more when it’s steady, not shouted.",
        "This fire inside you can build warmth, not just burn.",
        "It’s okay to feel angry — but you don’t need to let it rule you.",
        "Your calm is your strength — no one can take that away."
    ],

    "unmotivated": [
        "Motivation often follows action, not the other way — start small today.",
        "Even tiny steps matter — they are proof that you’re moving forward.",
        "You don’t have to do everything — just one thing is progress.",
        "Rest is not wasted time — it is part of building strength.",
        "Your value does not depend on productivity; you are enough already.",
        "Showing up today is a victory, even if you don’t feel like it.",
        "Energy ebbs and flows — today’s low will not last forever.",
        "It’s okay to take it slow — progress doesn’t have to be rushed.",
        "You can choose one gentle task and celebrate completing it.",
        "Self-compassion fuels motivation better than self-criticism ever will.",
        "Discipline means persistence, not punishment.",
        "You don’t need to see the whole path — just take the next step.",
        "Every effort you make, no matter how small, is worthy of recognition.",
        "You are not falling behind; you are moving at your pace.",
        "Sometimes surviving the day is already an achievement."
    ],

    "lonely": [
        "Loneliness does not mean you are unworthy — it means your heart is longing for connection.",
        "You are loved, even if it feels hard to see it right now.",
        "Connection can begin with one small step — a text, a call, a hello.",
        "You are not invisible. Your presence is valued in ways you may not realize.",
        "Being alone in a moment does not mean you are alone in the world.",
        "Loneliness is a signal, not a verdict — it points you toward belonging.",
        "Even in silence, your story matters and deserves to be heard.",
        "You are not forgotten — someone holds you in their thoughts today.",
        "You belong to the shared human experience; you are never fully isolated.",
        "Your voice matters — sharing it can bring others closer to you.",
        "Being alone can be painful, but it can also be a space for healing.",
        "You are worthy of companionship, love, and kindness.",
        "Someone out there needs the warmth only you can bring.",
        "Reaching out may feel scary, but it can open unexpected doors.",
        "Loneliness is temporary — your connections are waiting for you."
    ],

    "happy": [
        "Take a deep breath and savor this joy fully — it’s your reward for enduring the hard times.",
        "Happiness grows stronger when shared — who can you brighten today?",
        "Gratitude amplifies joy — name three things you’re thankful for right now.",
        "Celebrate not just the moment, but yourself for arriving here.",
        "Your smile could be the reason someone else finds hope today.",
        "Happiness is a reminder: better days always return, no matter how dark it gets.",
        "Anchor this joy in memory — it will be a reminder when times feel heavy.",
        "Your joy proves to others that healing and happiness are possible.",
        "Let your happiness ripple outward — it could change someone’s whole day.",
        "This is a reminder that you are capable of happiness again and again.",
        "Celebrate the small victories — they’re stepping stones to bigger ones.",
        "Joy is not selfish — it’s contagious, and the world benefits when you share it.",
        "Happiness is your gift — let it inspire kindness in others.",
        "Today, use your happiness to check on someone else who might be struggling.",
        "Happiness today is proof that resilience always pays off."
    ]
}


# --------------------------
# Fun Activities
# --------------------------
fun_activities = [
    "🎶 Listen to your favorite song and sing along.",
    "🖌️ Draw something silly or creative.",
    "💃 Do a 2-minute dance break.",
    "📖 Read a short inspiring story.",
    "🌿 Step outside and take 5 deep breaths.",
    "✍️ Write down 3 things you’re grateful for.",
    "🍫 Treat yourself to a small snack you enjoy."
]

# --------------------------
# Helper Functions
# --------------------------
def get_affirmation(mood: str) -> str:
    """Return a random affirmation based on mood."""
    mood_lower = mood.lower() if mood else "sad"
    if mood_lower in affirmations:
        return random.choice(affirmations[mood_lower])
    # fallback: pick a random from any mood
    all_affirmations = [a for mood_list in affirmations.values() for a in mood_list]
    return random.choice(all_affirmations)

def get_fun_activity() -> str:
    """Return a random fun activity."""
    return random.choice(fun_activities)

def apply_styles():
    """Apply consistent CSS styling to Streamlit pages."""
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

