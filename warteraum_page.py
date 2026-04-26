import streamlit as st
import os
from languages import translations
from database import get_current_ticket, get_waiting_tickets

# ---------------------------------------------------------
# Browser-Müll-Schutz
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# CSS für Karten
# ---------------------------------------------------------
st.markdown("""
    <style>
        .blue-card {
            background-color: #003A78;
            padding: 25px;
            border-radius: 20px;
            color: white;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Warteraum-Seite
# ---------------------------------------------------------
def show():
    lang = st.session_state.get("lang", "de")
    t = translations[lang]

    st.title(t["waiting_room"])

    aktuelles = get_current_ticket()
    waiting = get_waiting_tickets()

    # Aktuelles Ticket
    if aktuelles:
        st.markdown(f"""
            <div class="blue-card">
                {aktuelles['nummer']}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info(t["no_ticket_called"])

    st.write("### " + t["waiting_numbers"])

    # Warteliste
    if waiting:
        for tkt in waiting:
            st.markdown(f"""
                <div class="blue-card" style="font-size:28px;">
                    {tkt['nummer']}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info(t["no_more_tickets"])
