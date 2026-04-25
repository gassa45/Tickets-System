import streamlit as st
from database import create_ticket
from PIL import Image
import os
from languages import translations

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
logo = Image.open(image_path)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=250)

st.sidebar.image(logo, width=150)

st.set_page_config(page_title=t["pull_title"], layout="wide")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }

        .main-card {
            background-color: #1E90FF;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 100%;
            margin-top: 20px;
            text-align: left;
        }

        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: white;
            margin-bottom: 10px;
        }

        .main-text {
            font-size: 22px;
            color: white;
            margin-bottom: 20px;
        }

        .ticket-card {
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            text-align: center;
        }

        .ticket-number {
            font-size: clamp(40px, 8vw, 70px);
            font-weight: bold;
            color: #1E90FF;
        }

        .stButton>button {
            background-color: #1E90FF !important;
            color: white !important;
            border-radius: 12px;
            padding: 16px 25px;
            font-size: 24px;
            border: none;
            width: 100% !important;
            max-width: 400px;
            white-space: nowrap !important;
            margin-top: 20px;
        }

        .stButton>button:hover {
            background-color: #187bcd !important;
        }

        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        .info-visible {
            background-color: white;
            color: #008000;
            border-left: 6px solid #008000;
            padding: 22px;
            font-size: 26px;
            font-weight: bold;
            margin-top: 25px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="main-card">
        <div class="main-title">{t["pull_title"]}</div>
        <div class="main-text">{t["pull_info"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Button
# ---------------------------------------------------------
if st.button(t["pull_button"]):
    nummer = create_ticket()
    st.session_state["meine_nummer"] = nummer

    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{nummer}</span>
            <p style="color:#1E90FF; font-size:20px; margin-top:20px;">
                {t["pull_wait"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.switch_page("pages/2_Warteraum.py")

# ---------------------------------------------------------
# Info-Text immer sichtbar
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="info-visible">
        {t["pull_wait"]}
    </div>
    """,
    unsafe_allow_html=True
)
