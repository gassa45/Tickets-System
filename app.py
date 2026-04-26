# ---------------------------------------------------------
# Datei: app.py
# Hauptnavigation + Sidebar + Sprachsystem + Seitensteuerung
# ---------------------------------------------------------

import streamlit as st
from PIL import Image
import os
from languages import translations
import importlib

# ---------------------------------------------------------
# AUTOMATISCHER BROWSER-MÜLL-SCHUTZ
# ---------------------------------------------------------
def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean = []
    for line in lines:
        # Browser-Müll beginnt IMMER mit dieser Zeile
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean.append(line)

    # Wenn Müll gefunden → Datei reparieren
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
# Sprache initialisieren
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "de"

# ---------------------------------------------------------
# Navigation initialisieren
# ---------------------------------------------------------
if "nav" not in st.session_state:
    st.session_state.nav = "Startseite"

# ---------------------------------------------------------
# Sidebar Styling (DUNKELBLAU)
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #002B5B !important; /* Dunkelblau */
            padding-top: 20px;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
            font-size: 18px;
        }

        .nav-btn > button {
            background-color: #002B5B !important;
            color: white !important;
            border: 2px solid white !important;
            border-radius: 10px !important;
            padding: 10px !important;
            width: 100% !important;
            text-align: left !important;
            font-size: 18px !important;
        }

        .nav-btn > button:hover {
            background-color: white !important;
            color: #002B5B !important;
        }

        .logout-btn > button {
            background-color: #8B0000 !important; /* Dunkelrot */
            color: white !important;
            border-radius: 10px !important;
            padding: 10px !important;
            width: 100% !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR INHALT
# ---------------------------------------------------------
with st.sidebar:

    # Logo
    image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
    logo = Image.open(image_path)
    st.image(logo, width=180)

    st.write("---")

    # Sprache Auswahl mit Emoji
    lang_choice = st.selectbox(
        "🌐 Sprache / Language",
        ["🇩🇪 Deutsch", "🇬🇧 English", "🇫🇷 Français", "🇨🇳 中文"],
        index=["de", "en", "fr", "cn"].index(st.session_state.lang)
    )

    # Sprache speichern
    st.session_state.lang = {
        "🇩🇪 Deutsch": "de",
        "🇬🇧 English": "en",
        "🇫🇷 Français": "fr",
        "🇨🇳 中文": "cn"
    }[lang_choice]

    t = translations[st.session_state.lang]

    st.write("---")

    # Navigation
    st.markdown("### 📂 Navigation")

    if st.button("🏠 " + t["nav_home"], key="nav_home"):
        st.session_state.nav = "Startseite"

    if st.button("🧾 " + t["nav_customers"], key="nav_kunden"):
        st.session_state.nav = "Kunden"

    if st.button("⏳ " + t["nav_waiting"], key="nav_waiting"):
        st.session_state.nav = "Warteraum"

    if st.button("👨‍💼 " + t["nav_agent"], key="nav_agent"):
        st.session_state.nav = "Sachbearbeiter"

    st.write("---")

    # Logout
    if st.button("🚪 " + t["logout"], key="logout"):
        st.session_state.logged_in_sach = False
        st.session_state.nav = "Startseite"
        st.rerun()

# ---------------------------------------------------------
# SEITEN LADEN
# ---------------------------------------------------------

# Mapping der Seiten zu Modulen
pages = {
    "Startseite": "startseite",
    "Kunden": "kunden_page",
    "Warteraum": "warteraum_page",
    "Sachbearbeiter": "sachbearbeiter_page"
}

# Modul dynamisch laden
module_name = pages.get(st.session_state.nav)
module = importlib.import_module(module_name)

# show()-Funktion ausführen
module.show()
