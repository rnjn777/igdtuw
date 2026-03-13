import streamlit as st
from emotion_detector import detect_emotion
from llm_engine import get_supportive_response
from insight_engine import get_mental_insights, get_emoji_map
from ui_components import inject_custom_css, render_insight_panel, render_timeline

# --- Page Config ---
st.set_page_config(page_title="MindSentry", layout="wide", initial_sidebar_state="collapsed")
inject_custom_css()

# --- State Initialization ---
def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "mood_history" not in st.session_state:
        st.session_state.mood_history = ["neutral", "neutral", "neutral", "neutral"]
    if "current_insights" not in st.session_state:
        st.session_state.current_insights = None
    if "current_confidence" not in st.session_state:
        st.session_state.current_confidence = 0
    if "chat_active" not in st.session_state:
        st.session_state.chat_active = False
    if "pending_input" not in st.session_state:
        st.session_state.pending_input = None

init_state()

# Custom CSS is fully managed by ui_components.py now.

# --- Process Pending Input (deferred execution) ---
if st.session_state.pending_input:
    user_text = st.session_state.pending_input
    st.session_state.pending_input = None

    st.session_state.chat_active = True
    st.session_state.messages.append({"role": "user", "content": user_text})

    # Run emotion detection
    emotion, confidence = detect_emotion(user_text)
    st.session_state.current_confidence = confidence

    # Run insight engine
    insights = get_mental_insights(emotion, st.session_state.mood_history)
    st.session_state.current_insights = insights
    st.session_state.mood_history = insights["timeline_data"]

    # Get LLM response
    response = get_supportive_response(user_text, emotion)
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- HERO UI (shown before chat starts) ---
if not st.session_state.chat_active:
    
    def handle_hero_click(prompt):
        st.session_state.pending_input = prompt
        
    # The entirely redesigned glassmorphism homepage runs here
    from ui_components import render_hero
    render_hero(handle_hero_click)

# --- CHAT UI (shown after first message) ---
else:
    col_main, col_spacer, col_side = st.columns([2.5, 0.15, 1])

    with col_main:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"<div class='chat-message user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-message ai-msg'><b>✦ MindSentry</b><br><br>{msg['content']}</div>", unsafe_allow_html=True)

    with col_side:
        if st.session_state.current_insights:
            render_insight_panel(st.session_state.current_insights, st.session_state.current_confidence)
            render_timeline(st.session_state.mood_history, get_emoji_map())

# --- Chat Input (always visible at bottom) ---
user_input = st.chat_input("What would you like to reflect on?...")
if user_input and user_input.strip():
    st.session_state.pending_input = user_input
    st.rerun()
