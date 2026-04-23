import streamlit as st
import time
from database import (
    get_waiting_tickets,
    get_in_progress_tickets,
    call_next_ticket,
    finish_current_ticket,
)

st.title("🧑‍💼 Sachbearbeiter")

# ---------------------------------------------------------
# Session-State für gerade abgeschlossenes Ticket
# ---------------------------------------------------------
if "just_finished" not in st.session_state:
    st.session_state.just_finished = False

# ---------------------------------------------------------
# Wartende Tickets anzeigen (als Karten)
# ---------------------------------------------------------
st.subheader("Wartende Tickets")

waiting = get_waiting_tickets()

if waiting:
    for t in waiting:
        nr = t["nummer"]
        st.markdown(
            f"""
            <div style="
                background-color:#e0e0e0;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                margin-top: 8px;
            ">
                <span style="
                    font-size: 30px;
                    font-weight: bold;
                    color: #333;
                ">
                    {nr}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.write("Keine wartenden Tickets.")

# ---------------------------------------------------------
# Nächstes Ticket aufrufen
# ---------------------------------------------------------
if st.button("Nächstes Ticket aufrufen"):
    nummer = call_next_ticket()
    if nummer:
        st.success(f"Aufgerufen: {nummer}")
    else:
        st.warning("Keine Tickets mehr vorhanden.")

# ---------------------------------------------------------
# Aktuelles Ticket in Bearbeitung
# ---------------------------------------------------------
in_progress = get_in_progress_tickets()

st.subheader("Aktuell in Bearbeitung:")

if in_progress and not st.session_state.just_finished:
    aktuelle_nummer = in_progress[0]["nummer"]

    st.markdown(
        f"""
        <div style="
            background-color:#1E90FF;
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            margin-top: 10px;
        ">
            <span style="
                font-size: 60px;
                font-weight: bold;
                color: white;
            ">
                {aktuelle_nummer}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Kein Ticket in Bearbeitung.")

# ---------------------------------------------------------
# Ticket abschließen ("Fertig")
# ---------------------------------------------------------
if st.button("Fertig"):
    nummer = finish_current_ticket()
    if nummer:
        st.session_state.just_finished = True
        st.success(f"Ticket {nummer} abgeschlossen.")
        time.sleep(2)
        st.session_state.just_finished = False
        st.rerun()
    else:
        st.error("Kein Ticket in Bearbeitung.")
