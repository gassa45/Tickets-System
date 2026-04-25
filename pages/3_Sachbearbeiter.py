import streamlit as st
import time

from database import (
    get_waiting_tickets,
    get_in_progress_tickets,
    call_next_ticket,
    finish_current_ticket,
)

from PIL import Image
import os

# Absoluter Pfad zum Bild
image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
logo = Image.open(image_path)

# 3 Spalten erzeugen
col1, col2, col3 = st.columns([1, 2, 1])

# Bild in die mittlere Spalte
with col2:
    st.image(logo, width=250)



st.set_page_config(page_title="Sachbearbeiter", layout="centered")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Hintergrund */
        body {
            background-color: #f5f7fa;
        }

        /* BLAUE Karten */
        .ticket-card {
            background-color: #1E90FF;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-align: center;
            margin-top: 15px;
        }

        /* Nummer groß */
        .ticket-number {
            font-size: 60px;
            font-weight: bold;
            color: white;
        }

        /* Buttons – Abstand nach oben */
        .stButton {
            margin-top: 25px;
        }

        .stButton>button {
            background-color: #1E90FF;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: #187bcd;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.title("🧑‍💼 Sachbearbeiter")

if "just_finished" not in st.session_state:
    st.session_state.just_finished = False

st.subheader("Wartende Tickets")

waiting = get_waiting_tickets()

if waiting:
    for t in waiting:
        st.markdown(
            f"""
            <div class="ticket-card">
                <span class="ticket-number" style="font-size:40px;">{t['nummer']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.write("Keine wartenden Tickets.")

if st.button("Nächstes Ticket aufrufen"):
    nummer = call_next_ticket()
    if nummer:
        st.success(f"Aufgerufen: {nummer}")
    else:
        st.warning("Keine Tickets mehr vorhanden.")

st.subheader("Aktuell in Bearbeitung")

in_progress = get_in_progress_tickets()

if in_progress and not st.session_state.just_finished:
    aktuelle_nummer = in_progress[0]["nummer"]

    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{aktuelle_nummer}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Kein Ticket in Bearbeitung.")

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
