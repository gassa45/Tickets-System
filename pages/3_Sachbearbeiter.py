import streamlit as st
import time
from database import (
    get_waiting_tickets,
    get_in_progress_tickets,
    call_next_ticket,
    finish_current_ticket,
)
from PIL import Image
import os
from languages import translations

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

# Logo
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

st.set_page_config(page_title=t["agent_title"], layout="centered")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        body {
            background-color: #f5f7fa;
        }

        .ticket-card {
            background-color: #1E90FF;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-align: center;
            margin-top: 15px;
        }

        .ticket-number {
            font-size: 60px;
            font-weight: bold;
            color: white;
        }

        .stButton {
            margin-top: 25px;
        }

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
st.title(t["agent_title"])

if "just_finished" not in st.session_state:
    st.session_state.just_finished = False

# ---------------------------------------------------------
# Wartende Tickets
# ---------------------------------------------------------
st.subheader(t["waiting_tickets"])

waiting = get_waiting_tickets()

if waiting:
    for tkt in waiting:
        st.markdown(
            f"""
            <div class="ticket-card">
                <span class="ticket-number" style="font-size:40px;">{tkt['nummer']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.write(t["no_waiting"])

# Button: Nächstes Ticket
if st.button(t["call_next"]):
    nummer = call_next_ticket()
    if nummer:
        st.success(f"{t['call_next']}: {nummer}")
    else:
        st.warning(t["no_waiting"])

# ---------------------------------------------------------
# Aktuell in Bearbeitung
# ---------------------------------------------------------
st.subheader(t["in_progress"])

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
    st.write(t["none_in_progress"])

# Button: Fertig
if st.button(t["finish"]):
    nummer = finish_current_ticket()
    if nummer:
        st.session_state.just_finished = True
        st.success(f"{t['finished']} {nummer}")
        time.sleep(2)
        st.session_state.just_finished = False
        st.rerun()
    else:
        st.error(t["none_in_progress"])
