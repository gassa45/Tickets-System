import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets
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



st.set_page_config(page_title="TV Display", layout="wide")

# ---------------------------------------------------------
# TV-Display Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        body {
            background-color: #0A3D91;
        }

        .tv-card {
            background-color: #1E90FF;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
            text-align: center;
            margin-top: 30px;
        }

        .tv-number-big {
            font-size: 150px;
            font-weight: bold;
            color: white;
        }

        .tv-number-small {
            font-size: 80px;
            font-weight: bold;
            color: white;
        }

        h1, h2, h3, p {
            color: white !important;
            text-align: center;
        }

        /* Sidebar ausblenden */
        [data-testid="stSidebar"] {
            display: none;
        }
        .block-container {
            padding-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.title("📺 Warteraum – TV Display")

aktuelles_ticket = get_current_ticket()
waiting = get_waiting_tickets()

# ---------------------------------------------------------
# Aktuelles Ticket (riesig)
# ---------------------------------------------------------
st.markdown("## Aktuelles Ticket")

st.markdown(
    f"""
    <div class="tv-card">
        <span class="tv-number-big">{aktuelles_ticket if aktuelles_ticket else "—"}</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Nächste 3 Nummern
# ---------------------------------------------------------
st.markdown("## Nächste Nummern")

next_numbers = [t["nummer"] for t in waiting if t["nummer"] != aktuelles_ticket][:3]

if next_numbers:
    for nr in next_numbers:
        st.markdown(
            f"""
            <div class="tv-card">
                <span class="tv-number-small">{nr}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.markdown("<p>Keine weiteren Tickets.</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Auto-Refresh
# ---------------------------------------------------------
time.sleep(3)
st.rerun()
