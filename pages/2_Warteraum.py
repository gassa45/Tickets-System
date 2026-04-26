# ---------------------------------------------------------
# Datei: 2_Warteraum.py
# Warteraum – zeigt aktuelle Nummer + eigene Nummer + Warteschlange
# ---------------------------------------------------------

import streamlit as st
from PIL import Image
import os
from languages import translations
from database import (
    get_current_ticket,
    get_waiting_tickets
)

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

    # ---------------------------------------------------------
    # Styling – ALLE Karten dunkelblau
    # ---------------------------------------------------------
    st.markdown("""
        <style>
            body { background-color: #f5f7fa; }

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

            .small-number {
                font-size: 40px;
                font-weight: bold;
                color: white !important;
            }

            .info-text {
                color: white;
                font-size: 20px;
                margin-top: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Eigene Nummer aus URL oder Session
    # ---------------------------------------------------------
    query_params = st.query_params
    meine_nummer = query_params.get("ticket", [None])[0]

    if meine_nummer:
        st.session_state["meine_nummer"] = meine_nummer

    meine_nummer = st.session_state.get("meine_nummer", None)

    # ---------------------------------------------------------
    # Aktuelle Nummer
    # ---------------------------------------------------------
    aktuelles = get_current_ticket()

    st.markdown("## ⏳ " + t["waiting_room_title"])

    if aktuelles:
        st.markdown(
            f"""
            <div class="ticket-card">
                <div class="ticket-number">{aktuelles['nummer']}</div>
                <div class="info-text">{t["current_ticket"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info(t["no_ticket_called"])

    # ---------------------------------------------------------
    # Eigene Nummer anzeigen
    # ---------------------------------------------------------
    if meine_nummer:
        st.markdown(
            f"""
            <div class="ticket-card">
                <div class="ticket-number">{meine_nummer}</div>
                <div class="info-text">{t["your_ticket"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------------------------------------------------
    # Warteschlange anzeigen
    # ---------------------------------------------------------
    waiting = get_waiting_tickets()

    st.markdown("### " + t["waiting_numbers"])

    if waiting:
        for tkt in waiting:
            st.markdown(
                f"""
                <div class="ticket-card">
                    <div class="small-number">{tkt['nummer']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info(t["no_more_tickets"])

    # ---------------------------------------------------------
    # Automatische Aktualisierung alle 3 Sekunden
    # ---------------------------------------------------------
    st.markdown(
        """
        <script>
            setTimeout(function() {
                window.location.reload();
            }, 3000);
        </script>
        """,
        unsafe_allow_html=True
    )
