import streamlit as st
from database import create_ticket
from PIL import Image
import os
import qrcode
from io import BytesIO
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
# Sprache laden (Sidebar Dropdown)
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

st.session_state["lang"] = lang
t = translations[lang]


# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

BASE_URL = "https://revolution-ticketsystem.streamlit.app"

# ---------------------------------------------------------
# EINHEITLICHES DUNKELBLAUES DESIGN
# ---------------------------------------------------------
st.markdown("""
    <style>
        body { background-color: #f5f7fa; }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Hauptkarte */
        .main-card {
            background-color: #003A78 !important;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 100%;
            margin-top: 20px;
            text-align: left;
        }

        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: white !important;
            margin-bottom: 10px;
        }

        .main-text {
            font-size: 22px;
            color: white !important;
            margin-bottom: 20px;
        }

        /* Ticketkarte – jetzt dunkelblau */
        .ticket-card {
            background-color: #003A78 !important;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            text-align: center;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white !important;
        }

        .stButton>button {
            background-color: #003A78 !important;
            color: white !important;
            border-radius: 12px;
            padding: 16px 25px;
            font-size: 24px;
            border: none;
            width: 100% !important;
            max-width: 400px;
            margin-top: 20px;
        }

        textarea {
            font-size: 20px !important;
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


st.markdown("""
    <style>
        /* Dropdown Text schwarz machen */
        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)
# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
logo = Image.open(image_path)
st.sidebar.image(logo, width=250)

# ---------------------------------------------------------
# Hauptkarte
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="main-card">
        <div class="main-title">{t["pull_title"]}</div>
        <div class="main-text">{t["pull_info"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Beschreibung + Button
# ---------------------------------------------------------
beschreibung = st.text_area(
    "📝 Kurzbeschreibung (optional):",
    placeholder="Worum geht es? Bitte kurz beschreiben..."
)

if st.button(t["pull_button"]):

    nummer = create_ticket(beschreibung)
    st.session_state["meine_nummer"] = nummer
    st.session_state["beschreibung"] = beschreibung

    url = f"{BASE_URL}/Warteraum?ticket={nummer}"

    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_bytes = buffer.getvalue()

    # Ticketkarte – jetzt dunkelblau
    st.markdown(
        f"""
        <div class="ticket-card" style="margin-bottom:40px;">
            <span class="ticket-number">{nummer}</span>
            <p style="color:white; font-size:20px; margin-top:20px;">
                {t["pull_wait"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # QR-Code zentriert + Abstand
    import base64
    qr_base64 = base64.b64encode(qr_bytes).decode()

    st.markdown(
        f"""
        <div style="text-align:center; margin-top:40px;">
            <img src="data:image/png;base64,{qr_base64}" width="250">
            <p style="color:white; font-size:20px; margin-top:10px;">QR-Code</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Weiterleitung
    st.markdown(
        f"""
        <script>
            setTimeout(function() {{
                window.location.href = "{url}";
            }}, 2500);
        </script>
        """,
        unsafe_allow_html=True
    )
