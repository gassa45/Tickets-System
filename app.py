import streamlit as st
from PIL import Image
import os
from languages import translations
# ---------------------------------------------------------
# AUTOMATISCHER BROWSER-MÜLL-SCHUTZ
# ---------------------------------------------------------
import os, sys

def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean_lines = []
    for line in lines:
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break  # Alles danach löschen
        clean_lines.append(line)

    # Wenn Datei verändert wurde → neu schreiben
    if len(clean_lines) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean_lines)
        # App neu starten
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "de"

lang = st.sidebar.selectbox(
    "Sprache / Language / Langue / 语言",
    ["de", "en", "fr", "cn"],
    format_func=lambda x: {
        "de": "Deutsch",
        "en": "English",
        "fr": "Français",
        "cn": "中文"
    }[x]
)

st.session_state.lang = lang
t = translations[lang]

# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), ".", "revolution.png")
logo = Image.open(image_path)
st.sidebar.image(logo, width=150)


# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title=t["app_title"], layout="centered")


# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
# ---------------------------------------------------------
# Styling – DUNKELBLAUE KARTEN
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

        /* Dropdown lesbar machen */
        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        body { background-color: #f5f7fa; }

        .ticket-card {
            background-color: #003A78 !important;   /* DUNKELBLAU */
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.25);
            text-align: center;
            margin-top: 15px;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white !important;
        }

        .small-ticket {
            font-size: 45px;
            font-weight: bold;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }

        .main-card {
            background-color: #1E90FF;
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 100%;
            margin: 0;
            margin-top: 20px;
            text-align: left;
        }

        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: white;
            margin-bottom: 20px;
        }

        .main-text {
            font-size: 22px;
            color: white;
            margin-bottom: 10px;
        }

        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="main-card">
        <div class="main-title">{t["app_title"]}</div>
        <div class="main-text">{t["app_choose"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        /* Fix: Dropdown Text sichtbar machen */
        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Logout Button: Blau + weiße Schrift */
        [data-testid="stSidebar"] .stButton > button {
            background-color: #1E90FF !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 12px 20px !important;
            font-size: 18px !important;
            font-weight: bold !important;
        }

        /* Kein Hover-Farbwechsel */
        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: #1E90FF !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

