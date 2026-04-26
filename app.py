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
# Sprache
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "de"

lang = st.session_state["lang"]
t = translations[lang]

# ---------------------------------------------------------
# Custom Sidebar
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
        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
    if os.path.exists(image_path):
        st.image(image_path, width=160)

    st.session_state["lang"] = st.selectbox(
        "Language / Sprache",
        ["de", "en", "fr", "cn"],
        index=["de", "en", "fr", "cn"].index(st.session_state["lang"])
    )
    lang = st.session_state["lang"]
    t = translations[lang]

    pages = {
        t["nav_home"]: "startseite",
        t["nav_customers"]: "kunden_page",
        t["nav_waiting"]: "warteraum_page",
        t["nav_agent"]: "sachbearbeiter_page",
    }

    selected = st.radio("Navigation", list(pages.keys()))

# ---------------------------------------------------------
# Seite laden (OHNE show(), OHNE main())
# ---------------------------------------------------------
importlib.import_module(pages[selected])
