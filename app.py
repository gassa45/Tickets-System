import streamlit as st
import importlib
import os
from PIL import Image
from languages import translations

# ---------------------------------------------------------
# AUTOMATISCHER BROWSER-MÜLL-SCHUTZ
# ---------------------------------------------------------
def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean_lines = []
    for line in lines:
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean_lines.append(line)

    if len(clean_lines) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean_lines)
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Revolution Ticketsystem", layout="centered")

# ---------------------------------------------------------
# Einheitliches Sidebar-Design (dunkelblau, kein Hover)
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        [data-testid="stSidebar"] .stButton > button {
            background-color: #003A78 !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 10px 18px !important;
            font-size: 16px !important;
            font-weight: bold !important;
        }
        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: #003A78 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sprache wählen
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "de"

with st.sidebar:
    lang = st.selectbox(
        "Sprache / Language",
        options=["de", "en"],
        index=0 if st.session_state["lang"] == "de" else 1,
    )

st.session_state["lang"] = lang
t = translations[lang]

# ---------------------------------------------------------
# Logo in Sidebar
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
if os.path.exists(image_path):
    logo = Image.open(image_path)
    st.sidebar.image(logo, width=150)

# ---------------------------------------------------------
# Navigation
# ---------------------------------------------------------
pages = {
    t["home"]: "startseite",
    t["customers"]: "kunden_page",
    t["waiting_room"]: "warteraum_page",
    t["agent_title"]: "sachbearbeiter_page",
}

with st.sidebar:
    selected_label = st.radio("Navigation", list(pages.keys()))

module_name = pages[selected_label]

# ---------------------------------------------------------
# Seite laden (kein module.show(), nur Import)
# ---------------------------------------------------------
importlib.import_module(module_name)
