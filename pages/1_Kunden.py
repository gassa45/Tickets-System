# 1_Kunden.py

import streamlit as st
from database import create_ticket
from PIL import Image
import os
import qrcode
from io import BytesIO
from languages import translations
import base64

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Kunden", layout="centered")

# ---------------------------------------------------------
# Sidebar Styling (dunkelblau)
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
            padding-top: 30px;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Dropdown Text schwarz */
        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

#####################################
# Handy-Ansicht
########################################

st.markdown("""
    <style>
        @media (max-width: 768px) {
            [data-testid="stSidebar"] {
                width: 180px !important;
            }
            section[data-testid="stSidebar"] > div {
                width: 180px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @media (max-width: 768px) {
            .ticket-card {
                padding: 15px !important;
            }
            .ticket-number {
                font-size: 32px !important;
            }
            h1, h2, h3 {
                font-size: 22px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @media (max-width: 768px) {
            .stButton>button {
                padding: 8px 12px !important;
                font-size: 16px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Eigene Sidebar (Logo → Sprache → Navigation)
# ---------------------------------------------------------
with st.sidebar:

    # Logo ganz oben
    image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
    if os.path.exists(image_path):
        logo = Image.open(image_path)
        st.image(logo, width=250)

    # Sprache auswählen
    lang = st.selectbox(
        "Sprache / Language / Langue / 语言",
        ["de", "en", "fr", "cn"],
        format_func=lambda x: {
            "de": "Deutsch",
            "en": "English",
            "fr": "Français",
            "cn": "中文"
        }[x],
        index=["de", "en", "fr", "cn"].index(st.session_state.get("lang", "de"))
    )

    st.session_state["lang"] = lang
    t = translations[lang]

    st.markdown("---")

    # Navigation
    page = st.radio(
        t["navigation"],
        [t["nav_home"], t["nav_customers"], t["nav_waiting"], t["nav_agent"]]
    )

# ---------------------------------------------------------
# Navigation Logik
# ---------------------------------------------------------
if page == t["nav_home"]:
    st.switch_page("app.py")

elif page == t["nav_customers"]:
    pass  # wir sind bereits hier

elif page == t["nav_waiting"]:
    st.switch_page("pages/2_Warteraum.py")

elif page == t["nav_agent"]:
    st.switch_page("pages/3_Sachbearbeiter.py")

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

BASE_URL = "https://revolution-ticketsystem.streamlit.app"

# ---------------------------------------------------------
# EINHEITLICHES DUNKELBLAUES DESIGN
# ---------------------------------------------------------
st.markdown("""
    <style>
        body { background-color: #f5f7fa; }

        .main-card {
            background-color: #003A78 !important;
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
            color: white !important;
            margin-bottom: 10px;
        }

        .main-text {
            font-size: 22px;
            color: white !important;
            margin-bottom: 20px;
        }

        .ticket-card {
            background-color: #003A78 !important;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            text-align: center;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white !important;
        }

        .stButton>button {
            background-color: #003A78 !important;
            color: white !important;
            border-radius: 12px;
            padding: 16px 25px;
            font-size: 24px;
            border: none;
            width: 100% !important;
            max-width: 400px;
            margin-top: 20px;
        }

        textarea {
            font-size: 20px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Hauptkarte
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
# Beschreibung + Button
# ---------------------------------------------------------
st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)

st.markdown(f"""
<div style="
    font-size:20px;
    font-weight:600;
    margin-bottom:8px;
    color:#003A78;"> 📝 {t['description_title']}
</div>
""", unsafe_allow_html=True)

beschreibung = st.text_area(
    "",
    placeholder=t["description_placeholder"],
    height=120
)

st.markdown("""
<style>
textarea {
    border: 2px solid #003A78 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

if st.button(t["pull_button"]):

    nummer = create_ticket(beschreibung)
    st.session_state["meine_nummer"] = nummer
    st.session_state["beschreibung"] = beschreibung

    url = f"{BASE_URL}/Warteraum?ticket={nummer}"

    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_bytes = buffer.getvalue()
    qr_base64 = base64.b64encode(qr_bytes).decode()

    st.markdown(
        f"""
        <div class="ticket-card" style="margin-bottom:40px;">
            <span class="ticket-number">{nummer}</span>
            <p style="color:white; font-size:20px; margin-top:20px;">
                {t["pull_wait"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align:center; margin-top:40px;">
            <img src="data:image/png;base64,{qr_base64}" width="250">
            <p style="color:white; font-size:20px; margin-top:10px;">QR-Code</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <script>
            setTimeout(function() {{
                window.location.href = "{url}";
            }}, 2500);
        </script>
        """,
        unsafe_allow_html=True
    )
