import streamlit as st

def inject_custom_css():
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Sora:wght@400;600;700&display=swap');

    /* BASE THEME & LIQUID ANIMATION */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        color: #E2E8F0 !important;
    }
    
    .stApp {
        background: linear-gradient(-45deg, #0D1117, #1A202C, #0F172A, #1E1B4B);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Hide standard UI elements */
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="collapsedControl"] { display: none; }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 6rem !important;
        max-width: 1200px;
    }

    /* GLASSMORPHISM UTILS */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        padding: 2rem;
        transition: all 0.4s ease;
    }
    .glass-panel:hover {
        border-color: rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(0, 201, 255, 0.05);
    }

    /* GLOWING TEXT */
    .text-gradient {
        background: linear-gradient(135deg, #00C9FF, #8A2BE2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .text-gradient-purple {
        background: linear-gradient(135deg, #8A2BE2, #FF0080);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* HERO SECTION */
    .hero-container {
        text-align: center;
        margin-top: 5vh;
        margin-bottom: 4rem;
        animation: fadeIn 1s ease forwards;
        position: relative;
    }
    
    .sparkle-icon {
        font-size: 3.5rem;
        margin-bottom: 0px;
        animation: float 4s ease-in-out infinite, glow 2s alternate infinite;
        text-shadow: 0 0 20px rgba(0, 201, 255, 0.5);
    }
    .hero-title {
        font-family: 'Sora', sans-serif;
        font-size: 4.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-size: 1.8rem;
        font-weight: 300;
        color: #94A3B8;
        margin-bottom: 1.5rem;
    }
    .hero-desc {
        font-size: 1.1rem;
        color: #64748B;
        max-width: 650px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* STREAMLIT BUTTON OVERRIDES FOR CARDS */
    .stButton > button {
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        height: 160px !important;
        width: 100% !important;
        position: absolute;
        z-index: 10;
        cursor: pointer;
    }
    .card-wrapper { position: relative; margin-bottom: 2rem; }

    /* QUICK INTERACTION CARDS */
    .prompt-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.8rem;
        height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        text-align: center;
    }
    .prompt-card::before {
        content: ''; position: absolute; top:0; left:0; right:0; bottom:0; 
        opacity: 0; transition: opacity 0.4s; z-index: 0;
    }
    .prompt-card:hover { transform: translateY(-8px) scale(1.02); }
    .prompt-card:hover::before { opacity: 0.15; }
    
    .card-content { position: relative; z-index: 1; }
    .card-title { font-family: 'Sora', sans-serif; font-size: 1.2rem; font-weight: 600; color: #FFFFFF; margin-bottom: 0.5rem; }
    .card-sub { color: #94A3B8; font-size: 0.9rem; }

    .glow-blue::before { background: radial-gradient(circle at center, #58A6FF, transparent 60%); }
    .glow-purple::before { background: radial-gradient(circle at center, #8A2BE2, transparent 60%); }
    .glow-cyan::before { background: radial-gradient(circle at center, #00C9FF, transparent 60%); }
    .prompt-card:hover.glow-blue { border-color: rgba(88, 166, 255, 0.4); box-shadow: 0 0 20px rgba(88, 166, 255, 0.2); }
    .prompt-card:hover.glow-purple { border-color: rgba(138, 43, 226, 0.4); box-shadow: 0 0 20px rgba(138, 43, 226, 0.2); }
    .prompt-card:hover.glow-cyan { border-color: rgba(0, 201, 255, 0.4); box-shadow: 0 0 20px rgba(0, 201, 255, 0.2); }

    /* FEATURES GRID */
    .features-section {
        margin-top: 5rem;
        margin-bottom: 5rem;
    }
    .features-section h3 {
        text-align: center;
        margin-bottom: 3rem;
        font-family: 'Sora', sans-serif;
    }
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
    }
    .feature-item {
        text-align: center;
        padding: 2.5rem 1.5rem;
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    /* AI PIPELINE VISUALIZATION */
    .pipeline-section {
        margin-top: 4rem;
        padding: 3rem;
        text-align: center;
    }
    .pipeline-flow {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1.5rem;
        margin-top: 2rem;
        flex-wrap: wrap;
    }
    .pipeline-node {
        background: rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 1rem 1.5rem;
        border-radius: 30px;
        font-weight: 500;
        font-size: 0.95rem;
        position: relative;
        overflow: hidden;
    }
    .pipeline-node::after {
        content: ''; position: absolute; top:0; left:-100%; width: 50%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: sweep 3s infinite;
    }
    .pipeline-arrow { color: #58A6FF; font-size: 1.5rem; animation: pulse 2s infinite; }

    /* ANIMATIONS */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-10px); } 100% { transform: translateY(0px); } }
    @keyframes glow { 0% { text-shadow: 0 0 10px rgba(0, 201, 255, 0.3); } 100% { text-shadow: 0 0 30px rgba(0, 201, 255, 0.8), 0 0 60px rgba(138, 43, 226, 0.4); } }
    @keyframes sweep { 0% { left: -100%; } 100% { left: 200%; } }
    @keyframes pulse { 0% { opacity: 0.3; } 50% { opacity: 1; } 100% { opacity: 0.3; } }

    /* CHAT & EXISTING STYLES */
    .chat-message { padding: 1.5rem; border-radius: 16px; margin-bottom: 1.5rem; line-height: 1.7; animation: fadeIn 0.4s ease forwards; backdrop-filter: blur(10px); }
    .user-msg { background-color: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); margin-left: 2rem; }
    .ai-msg { background: rgba(0, 0, 0, 0.3); border-left: 3px solid #8A2BE2; margin-right: 2rem; color: #E2E8F0; }
    
    .insight-panel-container {
        background: rgba(13, 17, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px; padding: 1.8rem; backdrop-filter: blur(15px); margin-bottom: 1.5rem;
    }
    .panel-header { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1.5px; color: #94A3B8; margin-bottom: 1.2rem; font-weight: 600; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 0.8rem; }
    
    [data-testid="stMetricValue"] { font-size: 1.6rem !important; color: #FFFFFF !important; font-family: 'Sora', sans-serif !important; }
    [data-testid="stMetricLabel"] { color: #94A3B8 !important; }

    /* OVERRIDE BUTTONS for primary UI */
    .primary-btn-wrapper > .stButton > button {
        background: linear-gradient(135deg, #00C9FF, #58A6FF) !important;
        color: #000 !important;
        height: 50px !important;
        position: relative !important;
        border-radius: 25px !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease !important;
    }
    .primary-btn-wrapper > .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(0, 201, 255, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

def render_hero(on_click_fn):
    st.markdown("""
    <div class='hero-container'>
        <div class='sparkle-icon text-gradient'>✦</div>
        <div class='hero-title'>Mind<span class='text-gradient'>Sentry</span></div>
        <div class='hero-subtitle text-gradient-purple'>AI-Powered Mental Wellness Companion</div>
        <div class='hero-desc'>
            MindSentry combines Emotion AI, behavioral insights, and generative AI to detect emotional distress and provide supportive guidance for students in real-time.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Interaction Cards
    col1, col2, col3 = st.columns(3)
    
    cards = [
        ("I'm feeling very stressed right now.", "I'm feeling stressed", "Analyze My Anxiety", "glow-blue"),
        ("I need someone to talk to, I'm exhausted.", "I need to talk", "Connect & Vent", "glow-purple"),
        ("I can't stop thinking about exams, help me relax.", "Help me relax", "Guided Calming", "glow-cyan")
    ]
    
    for i, (prompt, title, subtitle, style) in enumerate(cards):
        with [col1, col2, col3][i]:
            st.markdown(f"""<div class='card-wrapper'>""", unsafe_allow_html=True)
            if st.button(f"Action: {title}", key=f"action_{i}", use_container_width=True):
                on_click_fn(prompt)
            st.markdown(f"""
            <div class='prompt-card {style}'>
                <div class='card-content'>
                    <div class='card-title'>{title}</div>
                    <div class='card-sub'>{subtitle}</div>
                </div>
            </div></div>
            """, unsafe_allow_html=True)

    # Features Section
    st.markdown("""
    <div class='features-section'>
        <h3 class='text-gradient'>Intelligent Capabilities</h3>
        <div class='feature-grid'>
            <div class='feature-item glass-panel'>
                <div class='feature-icon text-gradient'>🧠</div>
                <h4 style='color: white; font-family: "Sora"; margin-bottom: 0.5rem;'>Emotion Discovery</h4>
                <p style='color: #94A3B8; font-size: 0.9rem;'>Classifies nuanced emotional states using advanced NLP models directly from your text.</p>
            </div>
            <div class='feature-item glass-panel'>
                <div class='feature-icon text-gradient-purple'>🔥</div>
                <h4 style='color: white; font-family: "Sora"; margin-bottom: 0.5rem;'>Burnout Predictor</h4>
                <p style='color: #94A3B8; font-size: 0.9rem;'>Analyzes conversational timelines to predict and prevent deep academic burnout.</p>
            </div>
            <div class='feature-item glass-panel'>
                <div class='feature-icon' style='color: #58A6FF;'>✨</div>
                <h4 style='color: white; font-family: "Sora"; margin-bottom: 0.5rem;'>Generative Guidance</h4>
                <p style='color: #94A3B8; font-size: 0.9rem;'>Produces empathetic, context-aware responses and clinical coping techniques.</p>
            </div>
        </div>
    </div>
    
    <div class='pipeline-section glass-panel'>
        <h4 style='color: white; font-family: "Sora"; margin-bottom: 1rem;'>AI Pipeline Architecture</h4>
        <div class='pipeline-flow'>
            <div class='pipeline-node'>User Input</div>
            <i class='ri-arrow-right-line pipeline-arrow'>→</i>
            <div class='pipeline-node' style='border-color: #00C9FF;'>Emotion Detection</div>
            <i class='ri-arrow-right-line pipeline-arrow'>→</i>
            <div class='pipeline-node' style='border-color: #8A2BE2;'>Insight Engine</div>
            <i class='ri-arrow-right-line pipeline-arrow'>→</i>
            <div class='pipeline-node' style='border-color: #FF0080;'>Generative AI</div>
            <i class='ri-arrow-right-line pipeline-arrow'>→</i>
            <div class='pipeline-node' style='border-color: #00C9FF;'>Wellness Guidance</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_insight_panel(insights, confidence):
    st.markdown("<div class='insight-panel-container'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-header'>Mental Insight</div>", unsafe_allow_html=True)
    
    st.metric("Emotion Detected", f"{insights['emotion'].title()} ({int(confidence*100)}%)")
    
    colA, colB = st.columns(2)
    with colA: st.metric("Stress Trend", insights["stress_level"])
    with colB: st.metric("Sleep Risk", insights["sleep_risk"])
    
    st.markdown(f"""
    <div style='margin-top: 1rem; padding: 1.2rem; background: rgba(88, 166, 255, 0.05); border-left: 3px solid #00C9FF; border-radius: 8px;'>
        <div style='font-size:0.8rem; color:#94A3B8; text-transform: uppercase; letter-spacing: 1px; margin-bottom:0.5rem;'>Suggested Activity</div>
        <div style='color:#E2E8F0; font-weight:500; font-size: 0.95rem; line-height: 1.5;'>{insights['suggestion']}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_timeline(history, emoji_map):
    st.markdown("<div class='insight-panel-container'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-header'>Mood Timeline</div>", unsafe_allow_html=True)
    
    days = ["Msg 1", "Msg 2", "Msg 3", "Msg 4", "Now"]
    timeline_html = "<div style='display:flex; justify-content:space-between; margin-top:0.5rem;'>"
    
    for i, emotion in enumerate(history):
        emoji = emoji_map.get(emotion, "😐")
        day_label = days[i] if i < len(days) else "Now"
        timeline_html += f"<div style='text-align:center;'><div style='font-size:2rem; padding-bottom: 0.5rem;'>{emoji}</div><div style='font-size:0.75rem; color:#94A3B8; font-weight: 500;'>{day_label}</div></div>"
    
    timeline_html += "</div>"
    st.markdown(timeline_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
