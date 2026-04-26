import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets
from PIL import Image
import os
from languages import translations
# ---------------------------------------------------------
# AUTOMATISCHER BROWSER-MÜLL-SCHUTZ
# ---------------------------------------------------------
import os, sys

def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean_lines = []
    for line in lines:
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break  # Alles danach löschen
        clean_lines.append(line)

    # Wenn Datei verändert wurde → neu schreiben
    if len(clean_lines) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean_lines)
        # App neu starten
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# Ticketnummer aus URL lesen
# ---------------------------------------------------------
query_params = st.query_params
meine_nummer = query_params.get("ticket", None)

# Falls URL keine Nummer enthält → Session fallback
if not meine_nummer:
    meine_nummer = st.session_state.get("meine_nummer", None)

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
            background-color: #1E90FF;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-align: center;
            margin-top: 15px;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white;
        }

        .small-ticket {
            font-size: 45px;
            font-weight: bold;
            color: white;
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
# Titel
# ---------------------------------------------------------
st.title(t["waiting_room"])

# ---------------------------------------------------------
# Datenbank: aktuelles Ticket + Warteschlange
# ---------------------------------------------------------
aktuelles = get_current_ticket()
waiting = get_waiting_tickets()

# ---------------------------------------------------------
# Sound abspielen, wenn der Kunde dran ist
# ---------------------------------------------------------
if meine_nummer and aktuelles and aktuelles["nummer"] == meine_nummer:
    st.markdown("""
        <audio autoplay>
            <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
        </audio>
    """, unsafe_allow_html=True)
    st.success(t["called_now"])

# ---------------------------------------------------------
# Eigene Nummer anzeigen
# ---------------------------------------------------------
if meine_nummer:
    st.subheader(t["your_number"])
    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{meine_nummer}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# Aktuelles Ticket anzeigen
# ---------------------------------------------------------
st.subheader(t["current_ticket"])

if aktuelles:
    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{aktuelles['nummer']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Noch kein Ticket aufgerufen.")

# ---------------------------------------------------------
# Position in der Warteschlange
# ---------------------------------------------------------
if meine_nummer:
    alle = [tkt["nummer"] for tkt in waiting]

    if meine_nummer in alle:
        pos = alle.index(meine_nummer) + 1
        st.info(f"{t['queue_position']} **{pos}**")
    else:
        st.success(t["almost_called"])

# ---------------------------------------------------------
# Wartende anzeigen
# ---------------------------------------------------------
st.subheader(t["waiting_numbers"])

if waiting:
    for tkt in waiting:
        st.markdown(
            f"""
            <div class="ticket-card">
                <span class="small-ticket">{tkt['nummer']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info(t["no_more_tickets"])

# ---------------------------------------------------------
# Automatischer Refresh
# ---------------------------------------------------------
time.sleep(3)
st.rerun()
