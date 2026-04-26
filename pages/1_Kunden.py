import streamlit as st
from database import create_ticket
from PIL import Image
import os
import qrcode
from io import BytesIO
from languages import translations

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

BASE_URL = "https://revolution-ticketsystem.streamlit.app"

# ---------------------------------------------------------
# Styling – DEIN ALTES BLAUES DESIGN
# ---------------------------------------------------------
st.markdown("""
    <style>
        body { background-color: #f5f7fa; }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1E90FF !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Hauptkarte */
        .main-card {
            background-color: #1E90FF;
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
            color: white;
            margin-bottom: 10px;
        }

        .main-text {
            font-size: 22px;
            color: white;
            margin-bottom: 20px;
        }

        /* Ticketkarte */
        .ticket-card {
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            text-align: center;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: #1E90FF;
        }

        /* Blauer Button */
        .stButton>button {
            background-color: #1E90FF !important;
            color: white !important;
            border-radius: 12px;
            padding: 16px 25px;
            font-size: 24px;
            border: none;
            width: 100% !important;
            max-width: 400px;
            margin-top: 20px;
        }

        /* Beschreibung */
        textarea {
            font-size: 20px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
logo = Image.open(image_path)
st.sidebar.image(logo, width=150)

# ---------------------------------------------------------
# Hauptkarte (wie früher)
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

    # Ticket erstellen
    nummer = create_ticket(beschreibung)
    st.session_state["meine_nummer"] = nummer
    st.session_state["beschreibung"] = beschreibung

    # URL für QR-Code & Weiterleitung
    url = f"{BASE_URL}/Warteraum?ticket={nummer}"

    # QR-Code erzeugen
    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    # Ticketkarte anzeigen
    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{nummer}</span>
            <p style="color:#1E90FF; font-size:20px; margin-top:20px;">
                {t["pull_wait"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # QR-Code anzeigen
    st.image(buffer.getvalue(), caption="QR-Code", width=250)

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
