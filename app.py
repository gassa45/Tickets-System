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
# Grundkonfiguration
# ---------------------------------------------------------
st.set_page_config(page_title="Revolution Ticket-System", layout="wide")

if "lang" not in st.session_state:
    st.session_state.lang = "de"

if "nav" not in st.session_state:
    st.session_state.nav = "Startseite"

if "logged_in_sach" not in st.session_state:
    st.session_state.logged_in_sach = False

# ---------------------------------------------------------
# Sidebar Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #002B5B !important;
            padding-top: 20px;
        }
        [data-testid="stSidebar"] * {
            color: #E6E6E6 !important;
            font-size: 18px;
        }
        .nav-btn > button {
            background-color: #003A78 !important;
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
            background-color: #8B0000 !important;
            color: white !important;
            border-radius: 10px !important;
            padding: 10px !important;
            width: 100% !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Inhalt
# ---------------------------------------------------------
with st.sidebar:
    # Logo (nur in Sidebar, nicht oben auf der Startseite)
    image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
    if os.path.exists(image_path):
        st.image(Image.open(image_path), width=250)

    # Sprache
    lang_choice = st.selectbox(
        "🌐 Sprache / Language",
        ["🇩🇪 Deutsch", "🇬🇧 English", "🇫🇷 Français", "🇨🇳 中文"],
        index=["de", "en", "fr", "cn"].index(st.session_state.lang)
    )

    st.session_state.lang = {
        "🇩🇪 Deutsch": "de",
        "🇬🇧 English": "en",
        "🇫🇷 Français": "fr",
        "🇨🇳 中文": "cn"
    }[lang_choice]

    t = translations[st.session_state.lang]

    st.markdown("### 📂 Navigation")

    if st.button("🏠 " + t["nav_home"], key="nav_home"):
        st.session_state.nav = "Startseite"

    if st.button("🧾 " + t["nav_customers"], key="nav_kunden"):
        st.session_state.nav = "Kunden"

    if st.button("⏳ " + t["nav_waiting"], key="nav_waiting"):
        st.session_state.nav = "Warteraum"

    if st.button("👨‍💼 " + t["nav_agent"], key="nav_agent"):
        st.session_state.nav = "Sachbearbeiter"

    
# ---------------------------------------------------------
# Seiten-Routing
# ---------------------------------------------------------
pages = {
    "Startseite": "startseite",          # deine „Über uns“ / Startseite
    "Kunden": "kunden_page",
    "Warteraum": "warteraum_page",
    "Sachbearbeiter": "sachbearbeiter_page"
}

module_name = pages.get(st.session_state.nav, "startseite")
module = importlib.import_module(module_name)
module.show()