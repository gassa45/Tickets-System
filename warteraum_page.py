import streamlit as st
import os
from languages import translations
from database import get_current_ticket, get_waiting_tickets

def remove_browser_muell():
    file_path = os.path.abspath(__file__)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    clean = []
    for line in lines:
        if line.strip().startswith("# User's Edge browser tabs metadata"):
            break
        clean.append(line)
    if len(clean) != len(lines):
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(clean)
        st.rerun()

remove_browser_muell()

def show():
    lang = st.session_state.get("lang", "de")
    t = translations[lang]

    st.title(t["waiting_room"])

    aktuelles = get_current_ticket()
    waiting = get_waiting_tickets()

    if aktuelles:
        st.success(f"{t['current_ticket']}: {aktuelles['nummer']}")
    else:
        st.info(t["no_ticket_called"])

    st.write("### " + t["waiting_numbers"])

    if waiting:
        for tkt in waiting:
            st.write(f"• {tkt['nummer']}")
    else:
        st.info(t["no_more_tickets"])
