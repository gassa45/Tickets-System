import streamlit as st
from PIL import Image
import os
from languages import translations

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
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title=t["app_title"], layout="centered")

# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), ".", "revolution.png")
logo = Image.open(image_path)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=250)

st.sidebar.image(logo, width=250)

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
