import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets

st.set_page_config(page_title="Warteraum", layout="centered")

st.title("📢 Warteraum")

# ---------------------------------------------------------
# Aktuelles Ticket anzeigen
# ---------------------------------------------------------
aktuelles_ticket = get_current_ticket()

st.subheader("Aktuelles Ticket")

st.markdown(
    f"""
    <div style="
        background-color:#1E90FF;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-top: 10px;
    ">
        <span style="
            font-size: 80px;
            font-weight: bold;
            color: white;
        ">
            {aktuelles_ticket}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Wartende Tickets anzeigen (ALLE als Karten)
# ---------------------------------------------------------
st.subheader("Wartende Nummern")

waiting = get_waiting_tickets()

# aktuelles Ticket entfernen
waiting = [t for t in waiting if t != aktuelles_ticket]

if waiting:
    for nr in waiting:
        st.markdown(
            f"""
            <div style="
                background-color:#e0e0e0;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                margin-top: 10px;
            ">
                <span style="
                    font-size: 40px;
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
    st.write("Keine weiteren Tickets.")


# ---------------------------------------------------------
# Automatischer Refresh am ENDE
# ---------------------------------------------------------
time.sleep(3)
st.rerun()
