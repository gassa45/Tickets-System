import streamlit as st
from database import get_ticket_position
from PIL import Image
import os
from languages import translations

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# Einheitliches Styling – Dunkelblau (#003A78)
# ---------------------------------------------------------
st.markdown("""
    <style>
        body { background-color: #f5f7fa; }

        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        .main-card {
            background-color: #003A78 !important;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 100%;
            margin-top: 20px;
            text-align: left;
        }

        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: white !important;
            margin-bottom: 10px;
        }

        .main-text {
            font-size: 22px;
            color: white !important;
            margin-bottom: 20px;
        }

        .ticket-card {
            background-color: #003A78 !important;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.25);
            margin-top: 20px;
            text-align: center;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Logo (nur anzeigen, wenn Sachbearbeiter eingeloggt)
# ---------------------------------------------------------
if st.session_state.get("logged_in_sach", False):
    image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
    if os.path.exists(image_path):
        logo = Image.open(image_path)
        st.sidebar.image(logo, width=150)

    if st.sidebar.button(t["logout"]):
        st.session_state.logged_in_sach = False
        st.rerun()

# ---------------------------------------------------------
# Ticketnummer aus URL
# ---------------------------------------------------------
ticket = st.query_params.get("ticket", None)

if not ticket:
    st.error("Kein Ticket gefunden.")
    st.stop()

# ---------------------------------------------------------
# Hauptkarte
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="main-card">
        <div class="main-title">{t["waiting_room"]}</div>
        <div class="main-text">{t["wait_info"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Position abrufen
# ---------------------------------------------------------
position = get_ticket_position(ticket)

# ---------------------------------------------------------
# Ticketkarte
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="ticket-card">
        <span class="ticket-number">{ticket}</span>
        <p style="color:white; font-size:22px; margin-top:20px;">
            {t["your_position"]}: <b>{position}</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
