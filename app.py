import streamlit as st
import importlib
import os
from PIL import Image
from languages import translations

# ---------------------------------------------------------
# Browser-Müll-Schutz
# ---------------------------------------------------------
def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    clean = []
    for line in lines:
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean.append(line)
    if len(clean) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean)
        st.rerun()
remove_browser_muell()

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
# Custom Sidebar (Option C)
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
    # Logo oben
    image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
    if os.path.exists(image_path):
        st.image(image_path, width=160)

    # Sprache
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
# Seite laden
# ---------------------------------------------------------
module = importlib.import_module(pages[selected])
module.show()