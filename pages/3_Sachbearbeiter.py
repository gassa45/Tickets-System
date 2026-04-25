import streamlit as st
from database import get_waiting_tickets, call_next_ticket, finish_current_ticket, get_current_ticket
from languages import translations

# ---------------------------------------------------------
# Sprache laden
# ---------------------------------------------------------
lang = st.session_state.get("lang", "de")
t = translations[lang]

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1E90FF !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        body { background-color: #f5f7fa; }

        .ticket-box {
            background-color: #1E90FF;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-align: center;
            margin-top: 15px;
        }

        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white;
        }

        .beschreibung-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            border-left: 5px solid #1E90FF;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Titel
# ---------------------------------------------------------
st.title("Sachbearbeiter – Ticketverwaltung")

# ---------------------------------------------------------
# Aktuelles Ticket abrufen
# ---------------------------------------------------------
aktuelles = get_current_ticket()

if aktuelles:
    st.subheader("Aktuelles Ticket")

    # Ticketnummer anzeigen
    st.markdown(
        f"""
        <div class="ticket-box">
            <span class="ticket-number">{aktuelles['nummer']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Beschreibung anzeigen
    beschreibung = aktuelles.get("beschreibung", "")

    if beschreibung:
        st.markdown(
            f"""
            <div class="beschreibung-box">
                <b>Kurzbeschreibung:</b><br>{beschreibung}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Keine Beschreibung angegeben.")
else:
    st.info("Noch kein Ticket aufgerufen.")

# ---------------------------------------------------------
# Buttons: Nächstes Ticket / Ticket abschließen
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("➡️ Nächstes Ticket aufrufen"):
        next_ticket = call_next_ticket()
        if next_ticket:
            st.success(f"Ticket {next_ticket['nummer']} wurde aufgerufen.")
        else:
            st.warning("Keine wartenden Tickets.")

with col2:
    if st.button("✔️ Ticket abschließen"):
        finished = finish_current_ticket()
        if finished:
            st.success(f"Ticket {finished} wurde abgeschlossen.")
        else:
            st.warning("Kein Ticket in Bearbeitung.")

# ---------------------------------------------------------
# Wartende Tickets anzeigen
# ---------------------------------------------------------
st.subheader("Wartende Tickets")

waiting = get_waiting_tickets()

if waiting:
    for tkt in waiting:
        st.markdown(
            f"""
            <div class="ticket-box">
                <span class="ticket-number" style="font-size:45px;">{tkt['nummer']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("Keine wartenden Tickets.")
