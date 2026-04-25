import streamlit as st
from database import (
    get_waiting_tickets,
    call_next_ticket,
    finish_current_ticket,
    get_current_ticket
)
from languages import translations
from PIL import Image
import os

# ---------------------------------------------------------
# Page Config (MUSS GANZ OBEN SEIN)
# ---------------------------------------------------------
st.set_page_config(page_title="Sachbearbeiter", layout="centered")

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# LOGIN SYSTEM
# ---------------------------------------------------------
USERNAME = "gassa"
PASSWORD = "Gael2012"

if "logged_in_sach" not in st.session_state:
    st.session_state.logged_in_sach = False

def login_form():
    st.title(t["login_title"])
    username = st.text_input(t["username"])
    password = st.text_input(t["password"], type="password")

    if st.button(t["login"]):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in_sach = True
            st.success("OK")
            st.rerun()
        else:
            st.error(t["login_error"])

# Wenn NICHT eingeloggt → Login anzeigen und STOP
if not st.session_state.logged_in_sach:
    login_form()
    st.stop()

# ---------------------------------------------------------
# AB HIER NUR SICHTBAR, WENN EINGELOGGT
# ---------------------------------------------------------

# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
logo = Image.open(image_path)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=250)

st.sidebar.image(logo, width=150)

# Logout
if st.sidebar.button(t["logout"]):
    st.session_state.logged_in_sach = False
    st.rerun()

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

        .ticket-box {
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

        .beschreibung-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            border-left: 5px solid #1E90FF;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Logout Button: Blau + weiße Schrift */
        [data-testid="stSidebar"] .stButton > button {
            background-color: #1E90FF !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 12px 20px !important;
            font-size: 18px !important;
            font-weight: bold !important;
        }

        /* Kein Hover-Farbwechsel */
        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: #1E90FF !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Titel
# ---------------------------------------------------------
st.title(t["agent_title"])

# ---------------------------------------------------------
# Aktuelles Ticket
# ---------------------------------------------------------
aktuelles = get_current_ticket()

if aktuelles:
    st.subheader(t["current_ticket"])

    st.markdown(
        f"""
        <div class="ticket-box">
            <span class="ticket-number">{aktuelles['nummer']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    beschreibung = aktuelles.get("beschreibung", "")

    if beschreibung:
        st.markdown(
            f"""
            <div class="beschreibung-box">
                <b>{t["description"]}:</b><br>{beschreibung}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info(t["no_description"])
else:
    st.info(t["no_ticket_called"])

# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button(t["call_next"]):
        next_ticket = call_next_ticket()
        if next_ticket:
            st.success(f"{t['ticket_called']} {next_ticket['nummer']}")
        else:
            st.warning(t["no_more_tickets"])

with col2:
    if st.button(t["finish_ticket"]):
        finished = finish_current_ticket()
        if finished:
            st.success(f"{t['ticket_finished']} {finished}")
        else:
            st.warning(t["no_ticket_in_progress"])

# ---------------------------------------------------------
# Wartende Tickets
# ---------------------------------------------------------
st.subheader(t["waiting_numbers"])

waiting = get_waiting_tickets()

if waiting:
    for tkt in waiting:
        st.markdown(
            f"""
            <div class="ticket-box">
                <span class="ticket-number" style="font-size:45px;">{tkt['nummer']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info(t["no_more_tickets"])
