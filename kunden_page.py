import streamlit as st
import os
from languages import translations
from database import create_ticket

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

    st.title(t["pull_title"])
    st.write(t["pull_info"])

    if st.button(t["pull_button"]):
        nummer = create_ticket()
        st.success(f"{t['your_number']}: {nummer}")
        st.info(t["pull_wait"])
