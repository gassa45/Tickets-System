import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets

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

        /* Karten */
        .ticket-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            margin-top: 15px;
        }

        /* Nummer groß */
        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: #1E90FF;
        }

        /* Buttons */
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
st.title("📢 Warteraum")

aktuelles_ticket = get_current_ticket()

st.subheader("Aktuelles Ticket")

st.markdown(
    f"""
    <div class="ticket-card">
        <span class="ticket-number">{aktuelles_ticket if aktuelles_ticket else "—"}</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("Wartende Nummern")

waiting = get_waiting_tickets()
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

time.sleep(3)
st.rerun()
