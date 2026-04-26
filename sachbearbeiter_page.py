import streamlit as st
import os
from languages import translations
from database import (
    get_waiting_tickets,
    call_next_ticket,
    finish_current_ticket,
    get_current_ticket
)

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
# Sachbearbeiter-Seite
# ---------------------------------------------------------
def show():
    lang = st.session_state.get("lang", "de")
    t = translations[lang]

    # LOGIN
    if not st.session_state.get("logged_in_sach", False):

        st.markdown("""
            <div style='background-color:#003A78;padding:30px;border-radius:15px;
                        width:60%;margin:auto;margin-top:50px;color:white;
                        box-shadow:0 6px 20px rgba(0,0,0,0.3);'>
                <h2 style='text-align:center;'>🔐 Sachbearbeiter Login</h2>
            </div>
        """, unsafe_allow_html=True)

        username = st.text_input("Benutzername")
        password = st.text_input("Passwort", type="password")

        if st.button("Einloggen"):
            if username == "gassa" and password == "Gael2012":
                st.session_state.logged_in_sach = True
                st.success("Erfolgreich eingeloggt!")
                st.rerun()
            else:
                st.error("❌ Falscher Benutzername oder Passwort")

        return

    # AB HIER NUR SICHTBAR WENN EINGELOGGT
    st.title("👨‍💼 Sachbearbeiter Bereich")

    aktuelles = get_current_ticket()
    waiting = get_waiting_tickets()

    # Aktuelles Ticket
    if aktuelles:
        st.markdown(f"""
            <div class="blue-card">
                {aktuelles['nummer']}
            </div>
        """, unsafe_allow_html=True)

        if st.button("✔ Ticket abschließen"):
            finish_current_ticket()
            st.rerun()
    else:
        st.info("Noch kein Ticket in Bearbeitung.")

    st.write("### Wartende Tickets")

    if waiting:
        for tkt in waiting:
            if st.button(f"➡ Ticket {tkt['nummer']} aufrufen", key=f"call_{tkt['id']}"):
                call_next_ticket()
                st.rerun()
    else:
        st.info("Keine wartenden Tickets.")
