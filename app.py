import streamlit as st
import importlib
import os
from PIL import Image
from languages import translations

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Revolution Ticket-System", layout="wide")

# ---------------------------------------------------------
# Sprache (global in Session)
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "de"

lang = st.session_state["lang"]
t = translations[lang]

# ---------------------------------------------------------
# Sidebar Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
            padding-top: 30px;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
            font-size: 18px;
        }
        /* Dropdown-Inhalt schwarz, damit lesbar */
        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)
# ---------------------------------------------------------
# Sidebar Inhalt
# ---------------------------------------------------------
with st.sidebar:
    # Logo (liegt im Hauptordner neben app.py)
    image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
    if os.path.exists(image_path):
        st.image(image_path, width=160)

    # Sprache wählen
    st.session_state["lang"] = st.selectbox(
        "Language / Sprache",
        ["de", "en", "fr", "cn"],
        index=["de", "en", "fr", "cn"].index(st.session_state["lang"])
    )
    lang = st.session_state["lang"]
    t = translations[lang]
    # Navigation
    pages = {
        t["nav_home"]: "startseite",
        t["nav_customers"]: "kunden_page",
        t["nav_waiting"]: "warteraum_page",
        t["nav_agent"]: "sachbearbeiter_page",
    }

    selected = st.radio("Navigation", list(pages.keys()))

# ---------------------------------------------------------
# Seite laden (Modul importieren)
# ---------------------------------------------------------
importlib.import_module(pages[selected])