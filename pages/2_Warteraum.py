import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets
from style import load_logo

load_logo()


st.set_page_config(page_title="Warteraum", layout="centered")

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
            font-size: 70px;
            font-weight: bold;
            color: white;
        }

        /* Info-Text */
        .info-text {
            font-size: 20px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.title("📢 Warteraum")

# Eigene Nummer aus Session
meine_nummer = st.session_state.get("meine_nummer", None)

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

    st.success("🎉 Ihre Nummer wird jetzt aufgerufen!")


# ---------------------------------------------------------
# Eigene Nummer anzeigen
# ---------------------------------------------------------
if meine_nummer:
    st.subheader("Ihre Nummer")
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
st.subheader("Aktuelles Ticket")

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
    alle = [t["nummer"] for t in waiting]

    if meine_nummer in alle:
        position = alle.index(meine_nummer) + 1
        st.info(f"Ihre Position in der Warteschlange: **{position}**")
    else:
        st.success("🎉 Sie sind gleich dran oder werden bereits aufgerufen!")

# ---------------------------------------------------------
# Wartende anzeigen
# ---------------------------------------------------------
st.subheader("Wartende Nummern")

waiting = [t for t in waiting if t["nummer"] != aktuelles_ticket]

if waiting:
    for t in waiting:
        st.markdown(
            f"""
            <div class="ticket-card">
                <span class="ticket-number" style="font-size:45px;">{t['nummer']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.write("Keine weiteren Tickets.")

# ---------------------------------------------------------
# Automatischer Refresh
# ---------------------------------------------------------
time.sleep(3)
st.rerun()
