import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets
from PIL import Image
import os
from languages import translations

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
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
logo = Image.open(image_path)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=250)

st.sidebar.image(logo, width=150)

st.set_page_config(page_title=t["waiting_room"], layout="centered")

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
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.title(t["waiting_room"])

aktuelles_ticket = get_current_ticket()
waiting = get_waiting_tickets()

# ---------------------------------------------------------
# Sound abspielen, wenn der Kunde dran ist
# ---------------------------------------------------------
if meine_nummer and aktuelles_ticket == meine_nummer:
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

st.markdown(
    f"""
    <div class="ticket-card">
        <span class="ticket-number">{aktuelles_ticket if aktuelles_ticket else "—"}</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Position berechnen
# ---------------------------------------------------------
if meine_nummer:
    alle = [tkt["nummer"] for tkt in waiting]

    if meine_nummer in alle:
        position = alle.index(meine_nummer) + 1
        st.info(f"{t['queue_position']} **{position}**")
    else:
        st.success(t["almost_called"])

# ---------------------------------------------------------
# Wartende anzeigen
# ---------------------------------------------------------
st.subheader(t["waiting_numbers"])

waiting = [tkt for tkt in waiting if tkt["nummer"] != aktuelles_ticket]

if waiting:
    for tkt in waiting:
        st.markdown(
            f"""
            <div class="ticket-card">
                <span class="ticket-number" style="font-size:45px;">{tkt['nummer']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.write(t["no_more_tickets"])

# ---------------------------------------------------------
# Automatischer Refresh
# ---------------------------------------------------------
time.sleep(3)
st.rerun()
