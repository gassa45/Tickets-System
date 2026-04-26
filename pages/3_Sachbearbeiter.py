# ---------------------------------------------------------
# Datei: 3_Sachbearbeiter.py
# Sachbearbeiter – Tickets aufrufen, abschließen, Beschreibung anzeigen
# ---------------------------------------------------------

import streamlit as st
from PIL import Image
import os
from languages import translations
from database import (
    get_current_ticket,
    get_waiting_tickets,
    set_current_ticket,
    finish_ticket
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

    # Login-Schutz
    if not st.session_state.get("logged_in_sach", False):
        st.error(t["login_required"])
        return

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

            .description-box {
                background-color: #002B5B;
                color: white;
                padding: 20px;
                border-radius: 15px;
                margin-top: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                font-size: 20px;
            }

            .small-number {
                font-size: 40px;
                font-weight: bold;
                color: white !important;
            }

            .stButton>button {
                background-color: #1E90FF !important;
                color: white !important;
                border-radius: 12px;
                padding: 14px 20px;
                font-size: 22px;
                border: none;
                width: 100%;
                margin-top: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## 👨‍💼 " + t["agent_title"])

    # ---------------------------------------------------------
    # Aktuelles Ticket
    # ---------------------------------------------------------
    aktuelles = get_current_ticket()

    if aktuelles:
        st.markdown(
            f"""
            <div class="ticket-card">
                <div class="ticket-number">{aktuelles['nummer']}</div>
                <p style="color:white; font-size:20px; margin-top:10px;">
                    {t["current_ticket"]}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Beschreibung anzeigen
        if aktuelles.get("beschreibung"):
            st.markdown(
                f"""
                <div class="description-box">
                    {aktuelles['beschreibung']}
                </div>
                """,
                unsafe_allow_html=True
            )

        # Ticket abschließen
        if st.button(t["finish_ticket"]):
            finish_ticket(aktuelles["id"])
            st.rerun()

    else:
        st.info(t["no_ticket_called"])

    # ---------------------------------------------------------
    # Wartende Tickets
    # ---------------------------------------------------------
    waiting = get_waiting_tickets()

    st.markdown("### " + t["waiting_numbers"])

    if waiting:
        for tkt in waiting:
            if st.button(f"{t['call_ticket']} {tkt['nummer']}", key=f"call_{tkt['id']}"):
                set_current_ticket(tkt["id"])
                st.rerun()

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
