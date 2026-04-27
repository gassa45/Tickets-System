import streamlit as st
import time
from database import get_current_ticket, get_waiting_tickets
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
            break  # Alles danach löschen
        clean_lines.append(line)

    if len(clean_lines) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean_lines)
        st.rerun()

remove_browser_muell()

# ---------------------------------------------------------
# Sprache laden (Sidebar Dropdown)
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

st.session_state["lang"] = lang
t = translations[lang]

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# Ticketnummer aus URL lesen
# ---------------------------------------------------------
query_params = st.query_params
meine_nummer = query_params.get("ticket", None)

if not meine_nummer:
    meine_nummer = st.session_state.get("meine_nummer", None)

# ---------------------------------------------------------
# Styling – DUNKELBLAUE KARTEN
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #003A78 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        body { background-color: #f5f7fa; }

        .ticket-card {
            background-color: #003A78 !important;   /* DUNKELBLAU */
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.25);
            text-align: center;
            margin-top: 15px;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white !important;
        }

        .small-ticket {
            font-size: 45px;
            font-weight: bold;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

#####################################
#Ansicht für Handy
########################################

st.markdown("""
    <style>
        /* Sidebar auf Handy schmaler machen */
        @media (max-width: 768px) {
            [data-testid="stSidebar"] {
                width: 180px !important;
            }
            section[data-testid="stSidebar"] > div {
                width: 180px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @media (max-width: 768px) {
            .ticket-card {
                padding: 15px !important;
            }
            .ticket-number {
                font-size: 32px !important;
            }
            h1, h2, h3 {
                font-size: 22px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @media (max-width: 768px) {
            .stButton>button {
                padding: 8px 12px !important;
                font-size: 16px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        /* Dropdown Text schwarz machen */
        div[data-baseweb="select"] * {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)
# ---------------------------------------------------------
# Logo
# ---------------------------------------------------------
image_path = os.path.join(os.path.dirname(__file__), "..", "revolution.png")
logo = Image.open(image_path)
st.sidebar.image(logo, width=250)

# ---------------------------------------------------------
# Titel
# ---------------------------------------------------------
st.title(t["waiting_room"])

# ---------------------------------------------------------
# Datenbank
# ---------------------------------------------------------
aktuelles = get_current_ticket()
waiting = get_waiting_tickets()

# ---------------------------------------------------------
# Sound abspielen, wenn Kunde dran ist
# ---------------------------------------------------------
if meine_nummer and aktuelles and aktuelles["nummer"] == meine_nummer:
    st.markdown("""
        <audio autoplay>
            <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
        </audio>
    """, unsafe_allow_html=True)
    st.success(t["called_now"])

# ---------------------------------------------------------
# Eigene Nummer
# ---------------------------------------------------------
if meine_nummer:
    st.subheader(t["your_number"])
    st.markdown(f"""
        <div class="ticket-card">
            <span class="ticket-number">{meine_nummer}</span>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Aktuelles Ticket
# ---------------------------------------------------------
st.subheader(t["current_ticket"])

if aktuelles:
    st.markdown(f"""
        <div class="ticket-card">
            <span class="ticket-number">{aktuelles['nummer']}</span>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("Noch kein Ticket aufgerufen.")

# ---------------------------------------------------------
# Position in der Warteschlange
# ---------------------------------------------------------
if meine_nummer:
    alle = [tkt["nummer"] for tkt in waiting]

    if meine_nummer in alle:
        pos = alle.index(meine_nummer) + 1
        st.info(f"{t['queue_position']} **{pos}**")
    else:
        st.success(t["almost_called"])

# ---------------------------------------------------------
# Wartende anzeigen
# ---------------------------------------------------------
st.subheader(t["waiting_numbers"])

if waiting:
    for tkt in waiting:
        st.markdown(f"""
            <div class="ticket-card">
                <span class="small-ticket">{tkt['nummer']}</span>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info(t["no_more_tickets"])

# ---------------------------------------------------------
# Automatischer Refresh
# ---------------------------------------------------------
time.sleep(3)
st.rerun()
