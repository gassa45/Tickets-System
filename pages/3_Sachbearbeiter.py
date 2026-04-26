import streamlit as st
import time
import os
from languages import translations
from database import (
    get_waiting_tickets,
    get_in_progress_tickets,
    call_next_ticket,
    finish_current_ticket,
)

st.set_page_config(page_title="Sachbearbeiter", layout="centered")
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
# Styling – EINHEITLICH DUNKELBLAU
# ---------------------------------------------------------
st.markdown("""
    <style>
        /* Sidebar */
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

        /* DUNKELBLAUE Karten */
        .ticket-card {
            background-color: #003A78 !important;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.25);
            text-align: center;
            margin-top: 15px;
        }

        /* Nummer groß */
        .ticket-number {
            font-size: 60px;
            font-weight: bold;
            color: white !important;
        }

        /* Buttons */
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
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
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
