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
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Revolution Ticket System", layout="centered")

# ---------------------------------------------------------
# Global Styling (Desktop + Mobile)
# ---------------------------------------------------------
st.markdown("""
    <style>
        /* Sidebar dunkelblau */
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Hintergrund */
        body {
            background-color: #f5f7fa;
        }

        /* Ticket-Karten */
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

        /* Standard-Buttons */
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

        /* Dropdown Text schwarz */
        div[data-baseweb="select"] * {
            color: black !important;
        }

        /* Logout-Button in Sidebar explizit sichtbar machen */
        .stSidebar button[kind="secondary"] {
            background-color: #003A78 !important;
            color: white !important;
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: bold;
            border: none !important;
        }
        .stSidebar button[kind="secondary"]:hover {
            background-color: #003A78 !important;
            color: white !important;
        }

        /* Mobile-Optimierung */
        @media (max-width: 768px) {
            [data-testid="stSidebar"] {
                width: 180px !important;
            }
            section[data-testid="stSidebar"] > div {
                width: 180px !important;
            }
            .ticket-card {
                padding: 15px !important;
            }
            .ticket-number {
                font-size: 32px !important;
            }
            h1, h2, h3 {
                font-size: 22px !important;
            }
            .stButton>button {
                padding: 8px 12px !important;
                font-size: 16px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar: Sprache + Logo + Logout
# ---------------------------------------------------------
with st.sidebar:
    # Sprache
    lang = st.selectbox(
        "Sprache / Language / Langue / 语言",
        ["de", "en", "fr", "cn"],
        format_func=lambda x: {
            "de": "Deutsch",
            "en": "English",
            "fr": "Français",
            "cn": "中文"
        }[x],
        index=["de", "en", "fr", "cn"].index(st.session_state.get("lang", "fr"))
    )


    # Logo
    image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
    logo = Image.open(image_path)
    st.image(logo, width=250)

    # Logout nur wenn eingeloggt
    if st.session_state.get("logged_in", False):
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()

st.session_state["lang"] = lang
t = translations[lang]

# ---------------------------------------------------------
# Login-Schutz
# ---------------------------------------------------------
if not st.session_state.get("logged_in", False):
    st.title(t["login_title"])

    username = st.text_input(t["username"])
    password = st.text_input(t["password"], type="password")

    if st.button(t["login"]):
        # Platzhalter-Login – hier kannst du später echte Prüfung einbauen
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Erfolgreich eingeloggt!")
            st.rerun()
        else:
            st.error(t["login_error"])

    st.stop()

# ---------------------------------------------------------
# Inhalt – nur sichtbar, wenn eingeloggt
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
# ---------------------------------------------------------
# Nächstes Ticket aufrufen (mit schöner Anzeige)
# ---------------------------------------------------------
if st.button(t["call_next"]):
    nummer = call_next_ticket()
    if nummer:

        # Fallback, falls keine Beschreibung eingegeben wurde
        beschreibung = nummer["beschreibung"] or  t["no_description"]

        st.markdown(f"""
        <div style="
            background-color:#003A78;
            padding:15px;
            border-radius:12px;
            color:white;
            margin-top:15px;
            box-shadow:0 4px 10px rgba(0,0,0,0.25);
        ">
            <div style="font-size:22px; font-weight:700; margin-bottom:8px;">
                Ticket {nummer['nummer']}
            </div>
            <div style="font-size:18px; opacity:0.9;">
                {beschreibung}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(t["no_tickets_left"])

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

# ---------------------------------------------------------
# Ticket fertig
# ---------------------------------------------------------
if st.button(t["finish"]):
    nummer = finish_current_ticket()
    if nummer:
        st.session_state.just_finished = True
        st.success(f" {t["ticket_word"]} {nummer} {t["finished_word"]}")
        time.sleep(2)
        st.session_state.just_finished = False
        st.rerun()
    else:
        st.error(t["no_ticket_in_progress"])
