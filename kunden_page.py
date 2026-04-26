import streamlit as st
from database import create_ticket
from PIL import Image
import os
import qrcode
from io import BytesIO
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
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

BASE_URL = "https://revolution-ticketsystem.streamlit.app"

# ---------------------------------------------------------
# Styling – DUNKELBLAU (#003A78)
# ---------------------------------------------------------
st.markdown("""
    <style>
        body { background-color: #f5f7fa; }

        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

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

        .ticket-card {
            background-color: #003A78 !important;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.25);
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

# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
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

    # Ticketkarte (DUNKELBLAU)
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

    # QR-Code zentriert
    import base64
    qr_base64 = base64.b64encode(qr_bytes).decode()

    st.markdown(
        f"""
        <div style="text-align:center; margin-top:40px;">
            <img src="data:image/png;base64,{qr_base64}" width="250">
            <p style="color:#003A78; font-size:20px; margin-top:10px;">QR-Code</p>
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
