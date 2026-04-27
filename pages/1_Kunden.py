import streamlit as st
import qrcode
import os
from io import BytesIO
from PIL import Image
from languages import translations
from database import create_ticket

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Kunde", layout="centered")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
<style>
/* Hintergrund */
body {
    background-color: #f5f7fa;
}

/* Karte */
.ticket-card {
    background-color: #003A78 !important;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    text-align: center;
    margin-top: 20px;
    color: white !important;
}

/* Nummer */
.ticket-number {
    font-size: 60px;
    font-weight: bold;
    color: white !important;
}

/* Button */
.stButton>button {
    background-color: #003A78 !important;
    color: white !important;
    border-radius: 10px;
    padding: 12px 20px;
    font-size: 20px;
    border: none;
}
.stButton>button:hover {
    background-color: #002e5c !important;
}

/* Eingabefeld */
textarea {
    border: 2px solid #003A78 !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* Mobile */
@media (max-width: 768px) {
    .ticket-number {
        font-size: 36px !important;
    }
    .ticket-card {
        padding: 15px !important;
    }
    textarea {
        font-size: 15px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sprache
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# Titel
# ---------------------------------------------------------
st.title(t["pull_title"])
st.write(t["pull_info"])

# ---------------------------------------------------------
# Kurzbeschreibung (optional)
# ---------------------------------------------------------
st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)

st.markdown(f"""
<div style="
    font-size:20px;
    font-weight:600;
    margin-bottom:8px;
    color:#003A78;
">
    {t['description_title']}
</div>
""", unsafe_allow_html=True)

beschreibung = st.text_area(
    "",
    placeholder=t["description_placeholder"],
    height=120
)

# ---------------------------------------------------------
# Ticket ziehen
# ---------------------------------------------------------
if st.button(t["pull_button"]):
    nummer = create_ticket(beschreibung)

    if nummer:
        # QR-Code erzeugen
        qr = qrcode.make(nummer)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        buf.seek(0)

        # Ticketkarte anzeigen
        st.markdown(
            f"""
            <div class="ticket-card">
                <div class="ticket-number">{nummer}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.image(buf, caption="QR-Code", width=200)

        st.success(t["pull_wait"])

        # Automatische Weiterleitung nach 3 Sekunden
        st.markdown("""
            <meta http-equiv="refresh" content="3; url=/Warteraum">
        """, unsafe_allow_html=True)
