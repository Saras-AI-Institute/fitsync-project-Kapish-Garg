# import streamlit as st

# st.set_page_config(layout="wide", page_title="FitSync")

# st.title("Welcome to FitSync")

# st.write("Your personal health analytics dashboard")

# st.write("*Use the sidebar to navigate between pages*")

import streamlit as st

# ----------- PAGE CONFIG -----------
st.set_page_config(
    page_title="FitSync",
    layout="wide"
)

# ----------- SESSION STATE -----------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# ----------- HEADER -----------
col1, col2 = st.columns([8, 1])

with col1:
    st.title("💪 FitSync Dashboard")

with col2:
    toggle = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
    st.session_state.dark_mode = toggle

# ----------- THEME COLORS -----------
if st.session_state.dark_mode:
    bg_color = "#0E1117"
    text_color = "#FFFFFF"
    card_color = "#1c1f26"
    border_color = "#333"
    heading_color = "#00C9A7"
    sidebar_bg = "#161A22"
else:
    bg_color = "#F9F9F9"
    text_color = "#000000"
    card_color = "#FFFFFF"
    border_color = "#DDD"
    heading_color = "#007ACC"
    sidebar_bg = "#EAECEF"

# ----------- GLOBAL CSS -----------
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
            transition: all 0.3s ease;
        }}

        section[data-testid="stSidebar"] {{
            background-color: {sidebar_bg};
        }}

        section[data-testid="stSidebar"] * {{
            color: {text_color} !important;
        }}

        h1, h2, h3, h4, h5, h6, p, div, span, label {{
            color: {text_color} !important;
        }}

        .card {{
            background-color: {card_color};
            padding: 22px;
            border-radius: 18px;
            border: 1px solid {border_color};
            margin-bottom: 20px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
        }}

        .stButton>button {{
            background: linear-gradient(135deg, {heading_color}, #6a11cb);
            color: white;
            border-radius: 12px;
            padding: 10px 18px;
            border: none;
            font-weight: 600;
        }}

        .stButton>button:hover {{
            transform: scale(1.05);
            opacity: 0.9;
        }}

        .feature-list li {{
            margin-bottom: 8px;
        }}
    </style>
""", unsafe_allow_html=True)

# ----------- MAIN CONTENT -----------

st.markdown("""
<div class="card">
    <h2>🏋️ Your Personal Health Analytics Dashboard</h2>
    <p>Track your fitness, monitor your health, and stay consistent with your goals.</p>
</div>
""", unsafe_allow_html=True)

# ----------- FEATURES SECTION -----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>📊 Core Features</h4>
        <ul class="feature-list">
            <li>📊 Health Data Tracking</li>
            <li>📈 Progress Visualization</li>
            <li>🎯 Goal Setting</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>🤖 Smart Features</h4>
        <ul class="feature-list">
            <li>🤖 AI-Based Insights</li>
            <li>⏱️ Daily Activity Monitoring</li>
            <li>💡 Personalized Tips</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ----------- CTA BUTTON -----------
if st.button("🚀 Get Started"):
    st.success("Welcome! Use the sidebar to explore FitSync features.")

# ----------- INFO -----------
st.info("👉 Use the sidebar to navigate between different sections")