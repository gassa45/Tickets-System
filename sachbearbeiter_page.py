import streamlit as st
from database import (
    get_all_tickets,
    call_next_ticket,
    mark_ticket_done,
    get_ticket_description
)
from PIL import Image
import os
from languages import translations

# ---------------------------------------------------------
# AUTOMATISCHER BROWSER-MÜLL-SCHUTZ
# ---------------------------------------------------------
def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean_lines = []
    for line in lines:
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean_lines.append(line)

    if len(clean_lines) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean_lines)
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# Styling – Einheitlich Dunkelblau (#003A78)
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        .main-card {
            background-color: #003A78 !important;
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            margin-top: 20px;
            color: white !important;
        }

        .ticket-box {
            background-color: #003A78 !important;
            padding: 25px;
            border-radius: 15px;
            margin-top: 20px;
            color: white !important;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.25);
        }

        .ticket-number {
            font-size: 60px;
            font-weight: bold;
            color: white !important;
        }

        .stButton>button {
            background-color: #003A78 !important;
            color: white !important;
            border-radius: 12px;
            padding: 14px 20px;
            font-size: 20px;
            border: none;
            width: 100%;
            max-width: 350px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOGIN-BEREICH
# ---------------------------------------------------------
if "logged_in_sach" not in st.session_state:
    st.session_state.logged_in_sach = False

if not st.session_state.logged_in_sach:

    st.title(t["agent_title"])

    pw = st.text_input(t["password"], type="password")

    if st.button(t["login"]):
        if pw == "1234":  # Beispielpasswort
            st.session_state.logged_in_sach = True
            st.rerun()
        else:
            st.error(t["wrong_password"])

    st.stop()

# ---------------------------------------------------------
# Sidebar Logo + Logout (nur wenn eingeloggt)
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "revolution.png")
if os.path.exists(image_path):
    logo = Image.open(image_path)
    st.sidebar.image(logo, width=150)

if st.sidebar.button(t["logout"]):
    st.session_state.logged_in_sach = False
    st.rerun()

# ---------------------------------------------------------
# HAUPTANSICHT – Sachbearbeiter
# ---------------------------------------------------------
st.title(t["agent_title"])

tickets = get_all_tickets()

if not tickets:
    st.info(t["no_tickets"])
    st.stop()

# ---------------------------------------------------------
# NÄCHSTES TICKET ANZEIGEN
# ---------------------------------------------------------
st.subheader(t["next_ticket"])

if st.button(t["call_next"]):
    next_ticket = call_next_ticket()
    if next_ticket:
        st.session_state["current_ticket"] = next_ticket
        st.rerun()

current = st.session_state.get("current_ticket", None)

if current:
    beschreibung = get_ticket_description(current)

    st.markdown(
        f"""
        <div class="ticket-box">
            <div class="ticket-number">{current}</div>
            <p style="font-size:20px; margin-top:10px;">{beschreibung}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(t["mark_done"]):
        mark_ticket_done(current)
        st.session_state["current_ticket"] = None
        st.rerun()

# ---------------------------------------------------------
# WARTESCHLANGE ANZEIGEN
# ---------------------------------------------------------
st.subheader(t["queue"])

for ticket in tickets:
    st.markdown(
        f"""
        <div class="ticket-box" style="padding:15px;">
            <span style="font-size:30px; font-weight:bold;">{ticket}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
