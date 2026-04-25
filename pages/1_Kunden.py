import streamlit as st
from database import create_ticket


st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image("../revolution.png", width=250)
st.markdown("</div>", unsafe_allow_html=True)


st.set_page_config(page_title="Nummer ziehen", layout="wide")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }

        /* Hauptkarte – volle Breite */
        .main-card {
            background-color: #1E90FF;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 100%;
            margin-top: 20px;
            text-align: left;
        }

        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: white;
            margin-bottom: 10px;
        }

        .main-text {
            font-size: 22px;
            color: white;
            margin-bottom: 20px;
        }

        /* Ticket-Karte */
        .ticket-card {
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            text-align: center;
        }

        .ticket-number {
            font-size: clamp(40px, 8vw, 70px);
            font-weight: bold;
            color: #1E90FF;
        }

        /* BUTTON */
        .stButton>button {
            background-color: #1E90FF !important;
            color: white !important;
            border-radius: 12px;
            padding: 16px 25px;
            font-size: 24px;
            border: none;
            width: 100% !important;
            max-width: 400px;
            white-space: nowrap !important;
            margin-top: 20px;
        }

        .stButton>button:hover {
            background-color: #187bcd !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
            
                /* Info-Text eigene Box */
        .info-visible {
            background-color: white;
            color: #008000;              /* GRÜN */
            border-left: 6px solid #008000;
            padding: 22px;
            font-size: 26px;             /* GRÖSSER */
            font-weight: bold;           /* FETT */
            margin-top: 25px;
            border-radius: 5px;
        }

    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.markdown("""
<div class="main-card">
    <div class="main-title">🎫 Nummer ziehen</div>
    <div class="main-text">Bitte drücken Sie auf den Button, um Ihre Wartenummer zu erhalten.</div>
</div>
""", unsafe_allow_html=True)

# Button
if st.button("Nummer ziehen"):
    nummer = create_ticket()
    st.session_state["meine_nummer"] = nummer

    # Ticket + Info-Text in EINER weißen Karte → IMMER sichtbar
    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{nummer}</span>
            <p style="color:#1E90FF; font-size:20px; margin-top:20px;">
                Bitte warten Sie, bis Ihre Nummer aufgerufen wird.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.switch_page("pages/2_Warteraum.py")

# ---------------------------------------------------------
# Info-Text IMMER sichtbar, NICHT in IF-Bedingung
# ---------------------------------------------------------
st.markdown("""
<div class="info-visible">
    Bitte warten Sie, bis Ihre Nummer aufgerufen wird.
</div>
""", unsafe_allow_html=True)
