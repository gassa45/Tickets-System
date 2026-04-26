import streamlit as st
import os
from languages import translations
from database import (
    get_current_ticket,
    get_waiting_tickets,
    set_current_ticket,
    finish_ticket
)

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

    if not st.session_state.get("logged_in_sach", False):
        st.error(t["login_error"])
        return

    st.title(t["agent_title"])

    aktuelles = get_current_ticket()
    waiting = get_waiting_tickets()

    if aktuelles:
        st.success(f"{t['current_ticket']}: {aktuelles['nummer']}")
        if st.button(t["finish_ticket"]):
            finish_ticket(aktuelles["id"])
            st.rerun()
    else:
        st.info(t["no_ticket_called"])

    st.write("### " + t["waiting_tickets"])

    if waiting:
        for tkt in waiting:
            if st.button(f"{t['call_next']} {tkt['nummer']}", key=f"call_{tkt['id']}"):
                set_current_ticket(tkt["id"])
                st.rerun()
    else:
        st.info(t["no_waiting"])
