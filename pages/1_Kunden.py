# ---------------------------------------------------------
# Datei: 1_Kunden.py
# Kunden-Seite – Ticket ziehen + QR-Code
# ---------------------------------------------------------

import streamlit as st
from PIL import Image
import os
import qrcode
from io import BytesIO
from languages import translations
from database import create_ticket
import base64

# ---------------------------------------------------------
# AUTOMATISCHER BROWSER-MÜLL-SCHUTZ
# ---------------------------------------------------------
def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean = []
    for line in lines:
        # Browser-Müll beginnt IMMER mit dieser Zeile
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean.append(line)

    # Wenn Müll gefunden → Datei reparieren
    if len(clean) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean)
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# HAUPTFUNKTION DER SEITE
# ---------------------------------------------------------
def show():

    # Sprache laden
    lang = st.session_state.get("lang", "de")
    t = translations[lang]

    BASE_URL = "https://revolution-ticketsystem.streamlit.app"

    # ---------------------------------------------------------
    # Styling – ALLE Karten dunkelblau
    # ---------------------------------------------------------
    st.markdown("""
        <style>
            body { background-color: #f5f7fa; }

            .main-card {
                background-color: #002B5B; /* Dunkelblau */
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

            .ticket-card {
                background-color: #002B5B; /* Dunkelblau */
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                margin-top: 20px;
                text-align: center;
            }

            .ticket-number {
                font-size: 70px;
                font-weight: bold;
                color: white !important;
            }

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
        </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Hauptkarte (Titel + Info)
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

    # Beschreibung
    beschreibung = st.text_area("📝 Kurzbeschreibung (optional):")

    # ---------------------------------------------------------
    # Ticket ziehen
    # ---------------------------------------------------------
    if st.button(t["pull_button"]):

        nummer = create_ticket(beschreibung)
        st.session_state["meine_nummer"] = nummer

        url = f"{BASE_URL}/Warteraum?ticket={nummer}"

        # QR-Code erzeugen
        qr = qrcode.make(url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        qr_bytes = buffer.getvalue()
        qr_base64 = base64.b64encode(qr_bytes).decode()

        # Ticketkarte (dunkelblau)
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
        st.markdown(
            f"""
            <div style="text-align:center; margin-top:40px;">
                <img src="data:image/png;base64,{qr_base64}" width="250">
                <p style="color:#002B5B; font-size:20px; margin-top:10px;">QR-Code</p>
            </div>
            """,
            unsafe_allow_html=True
        )
