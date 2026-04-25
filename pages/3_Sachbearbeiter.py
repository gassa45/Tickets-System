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
st.title(t["agent_title"])

# ---------------------------------------------------------
# Aktuelles Ticket abrufen
# ---------------------------------------------------------
aktuelles = get_current_ticket()

if aktuelles:
    st.subheader(t["current_ticket"])

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
                <b>{t["description"]}:</b><br>{beschreibung}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info(t["no_description"])
else:
    st.info(t["no_ticket_called"])

# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button(t["call_next"]):
        next_ticket = call_next_ticket()
        if next_ticket:
            st.success(f"{t['ticket_called']} {next_ticket['nummer']}")
        else:
            st.warning(t["no_more_tickets"])

with col2:
    if st.button(t["finish_ticket"]):
        finished = finish_current_ticket()
        if finished:
            st.success(f"{t['ticket_finished']} {finished}")
        else:
            st.warning(t["no_ticket_in_progress"])

# ---------------------------------------------------------
# Wartende Tickets anzeigen
# ---------------------------------------------------------
st.subheader(t["waiting_numbers"])

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
    st.info(t["no_more_tickets"])
