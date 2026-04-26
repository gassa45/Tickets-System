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
st.set_page_config(page_title="Revolution Ticketsystem", layout="centered")

# ---------------------------------------------------------
# Sprache wählen
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "de"

with st.sidebar:
    lang = st.selectbox(
        "Language / Sprache",
        options=["de", "en", "fr", "cn"],
        index=["de", "en", "fr", "cn"].index(st.session_state["lang"])
    )

st.session_state["lang"] = lang
t = translations[lang]

# ---------------------------------------------------------
# Sidebar Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
if os.path.exists(image_path):
    logo = Image.open(image_path)
    st.sidebar.image(logo, width=150)

# ---------------------------------------------------------
# Navigation (NEUE KEYS!)
# ---------------------------------------------------------
pages = {
    t["nav_home"]: "startseite",
    t["nav_customers"]: "kunden_page",
    t["nav_waiting"]: "warteraum_page",
    t["nav_agent"]: "sachbearbeiter_page",
}

with st.sidebar:
    selected_label = st.radio("Navigation", list(pages.keys()))

module_name = pages[selected_label]

# ---------------------------------------------------------
# Seite laden
# ---------------------------------------------------------
importlib.import_module(module_name)
