import streamlit as st
import os
from PIL import Image
from languages import translations

# ---------------------------------------------------------
# BROWSER-MÜLL-KILLER 3.0 (unkaputtbar)
# ---------------------------------------------------------
def remove_browser_muell():
    markers = [
        "# User's Edge browser tabs metadata",
        "edge_all_open_tabs = [",
        "The edge_all_open_tabs metadata provides important context"
    ]

    file_path = os.path.abspath(__file__)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        return

    clean_lines = []
    skip = False

    for line in lines:
        if any(marker in line for marker in markers):
            skip = True
        if not skip:
            clean_lines.append(line)

    if clean_lines != lines:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(clean_lines)
        except:
            return
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# Sprache + Logo in Sidebar
# ---------------------------------------------------------
with st.sidebar:
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

    image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
    logo = Image.open(image_path)
    st.image(logo)

st.session_state["lang"] = lang
t = translations[lang]

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title=t["about_title"], layout="centered")

# ---------------------------------------------------------
# Sidebar + Dropdown + Responsive Logo CSS
# ---------------------------------------------------------
st.markdown("""
    <style>
        /* Sidebar dunkelblau */
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

        /* Responsive Sidebar Logo */
        [data-testid="stSidebar"] img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 250px !important;      /* Desktop */
            max-width: 80% !important;    /* Falls Sidebar kleiner ist */
            height: auto !important;
        }

        /* Tablet */
        @media (max-width: 1200px) {
            [data-testid="stSidebar"] img {
                width: 200px !important;
            }
        }

        /* Handy */
        @media (max-width: 768px) {
            [data-testid="stSidebar"] img {
                width: 150px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CSS für Animationen + Layout
# ---------------------------------------------------------
st.markdown("""
    <style>
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .fade {
            animation: fadeIn 1.2s ease-out;
        }

        .about-card {
            background: linear-gradient(135deg, #1E90FF, #0066CC);
            padding: 50px;
            border-radius: 30px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.25);
            width: 85%;
            margin: auto;
            margin-top: 50px;
            text-align: center;
            color: white;
        }
        .about-title {
            font-size: 48px;
            font-weight: 800;
            margin-bottom: 20px;
        }
        .about-sub {
            font-size: 22px;
            margin-bottom: 40px;
            opacity: 0.95;
        }

        .about-section {
            background-color: white;
            color: #003A78;
            padding: 30px;
            border-radius: 20px;
            width: 85%;
            margin: 40px auto;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            font-size: 20px;
            line-height: 1.6;
        }
        .about-section h3 {
            color: #002B5B;
            font-weight: 700;
        }

        .contact-box {
            background-color: #003A78;
            color: white;
            padding: 35px;
            border-radius: 20px;
            width: 85%;
            margin: 40px auto;
            text-align: center;
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        }
        .contact-box h3 {
            font-size: 28px;
            margin-bottom: 15px;
        }
        .contact-box p {
            font-size: 20px;
            margin: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt – STARTSEITE MIT SPRACH-KEYS
# ---------------------------------------------------------

st.markdown(f"""
    <div class="about-card fade">
        <div class="about-title">{t["about_title"]}</div>
        <div class="about-sub">{t["about_sub"]}</div>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="about-section fade">
        <h3>{t["about_us_title"]}</h3>
        <p>{t["about_us_text"]}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="about-section fade">
        <h3>{t["mission_title"]}</h3>
        <p>{t["mission_text"]}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="about-section fade">
        <h3>{t["why_title"]}</h3>
        <ul>
            <li>{t["why_1"]}</li>
            <li>{t["why_2"]}</li>
            <li>{t["why_3"]}</li>
            <li>{t["why_4"]}</li>
            <li>{t["why_5"]}</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="contact-box fade">
        <h3>{t["contact_title"]}</h3>
        <p>{t["contact_mail"]}</p>
        <p>{t["contact_phone"]}</p>
        <p>{t["contact_location"]}</p>
    </div>
""", unsafe_allow_html=True)
