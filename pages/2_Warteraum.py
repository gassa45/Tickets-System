import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets

st.set_page_config(page_title="Warteraum", layout="centered")

st.title("📢 Warteraum")

# ---------------------------------------------------------
# Aktuelles Ticket anzeigen
# ---------------------------------------------------------
aktuelles_ticket = get_current_ticket()   # z.B. 1, 2, 3 …

formatted_current = (
    f"A{int(aktuelles_ticket):03d}" if aktuelles_ticket else "—"
)

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
            {formatted_current}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Wartende Tickets anzeigen
# ---------------------------------------------------------
st.subheader("Wartende Nummern")

waiting = get_waiting_tickets()

# aktuelles Ticket aus Liste entfernen
waiting = [t for t in waiting if t["nummer"] != aktuelles_ticket]

if waiting:
    for t in waiting:
        nr = f"A{int(t['nummer']):03d}"
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
# Automatischer Refresh
# ---------------------------------------------------------
time.sleep(3)
st.rerun()
