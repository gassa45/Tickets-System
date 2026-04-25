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
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1E90FF !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        body { background-color: #f5f7fa; }

        .ticket-card {
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            text-align: center;
        }

        .ticket-number {
            font-size: 60px;
            font-weight: bold;
            color: #1E90FF;
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
# Titel & Info
# ---------------------------------------------------------
st.title(t["pull_title"])
st.write(t["pull_info"])

# ---------------------------------------------------------
# Button: Ticket ziehen
# ---------------------------------------------------------
if st.button(t["pull_button"]):

    # 📝 Beschreibung vom Kunden
    beschreibung = st.text_area(
        "📝 Kurzbeschreibung (optional):",
        placeholder="Worum geht es? Bitte kurz beschreiben..."
    )

    # Ticket erstellen + Beschreibung speichern
    nummer = create_ticket(beschreibung)
    st.session_state["meine_nummer"] = nummer
    st.session_state["beschreibung"] = beschreibung

    # URL für QR-Code & Weiterleitung
    url = f"{BASE_URL}/Warteraum?ticket={nummer}"

    # QR-Code erzeugen
    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    # Ticket anzeigen
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

    # Automatische Weiterleitung nach 2.5 Sekunden
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
