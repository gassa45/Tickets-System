import streamlit as st
import time
import os
from PIL import Image
from languages import translations
from database import (
    get_waiting_tickets,
    get_in_progress_tickets,
    call_next_ticket,
    finish_current_ticket,
)

# ---------------------------------------------------------
# LOGOUT BUTTON (nur wenn eingeloggt)
# ---------------------------------------------------------
with st.sidebar:
    if st.session_state.get("logged_in", False):
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Sachbearbeiter", layout="centered")

# ---------------------------------------------------------
# Sprache + Logo in Sidebar
# ---------------------------------------------------------
with st.sidebar:
    lang = st.selectbox(
        "Sprache / Language / Langue / 语言",
        ["de", "en", "fr", "cn"],
        format_func=lambda x: {
            "de": "Deutsch",
            "en": "English",
            "fr": "Français",
            "cn": "中文"
        }[x],
        index=["de", "en", "fr", "cn"].index(st.session_state.get("lang", "de"))
    )

    image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
    logo = Image.open(image_path)
    st.image(logo, width=250)

st.session_state["lang"] = lang
t = translations[lang]

# ---------------------------------------------------------
# LOGIN-SCHUTZ
# ---------------------------------------------------------
if not st.session_state.get("logged_in", False):

    st.title("Sachbearbeiter Login")

    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Erfolgreich eingeloggt!")
            st.rerun()
        else:
            st.error("Falsche Zugangsdaten")

    st.stop()  # verhindert Zugriff auf die Seite ohne Login

# ---------------------------------------------------------
# Styling – EINHEITLICH DUNKELBLAU
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        body {
            background-color: #f5f7fa;
        }

        .ticket-card {
            background-color: #003A78 !important;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.25);
            text-align: center;
            margin-top: 15px;
        }

        .ticket-number {
            font-size: 60px;
            font-weight: bold;
            color: white !important;
        }

        .stButton {
            margin-top: 25px;
        }

        .stButton>button {
            background-color: #003A78 !important;
            color: white !important;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
        }

        .stButton>button:hover {
            background-color: #002e5c !important;
        }

        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# INHALT – NUR SICHTBAR WENN EINGELOGGT
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
