import streamlit as st
import os
from PIL import Image
from languages import translations

################
####Logout Button
################

with st.sidebar:
    if st.session_state.get("logged_in", False):
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()


# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Revolution Ticket System", layout="centered")

# ---------------------------------------------------------
# Sidebar Styling (dunkelblau)
# ---------------------------------------------------------
st.markdown("""
    <style>
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
    </style>
""", unsafe_allow_html=True)

#####################################
#Ansicht für Handy
########################################

st.markdown("""
    <style>
        /* Sidebar auf Handy schmaler machen */
        @media (max-width: 768px) {
            [data-testid="stSidebar"] {
                width: 180px !important;
            }
            section[data-testid="stSidebar"] > div {
                width: 180px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @media (max-width: 768px) {
            .ticket-card {
                padding: 15px !important;
            }
            .ticket-number {
                font-size: 32px !important;
            }
            h1, h2, h3 {
                font-size: 22px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @media (max-width: 768px) {
            .stButton>button {
                padding: 8px 12px !important;
                font-size: 16px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Sidebar: Sprache + Logo (fest 250px)
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
    st.image(logo, width=250)

st.session_state["lang"] = lang
t = translations[lang]

# ---------------------------------------------------------
# CSS für Animationen + Layout (DEIN DESIGN)
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
