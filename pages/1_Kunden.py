import streamlit as st
from database import create_ticket

st.set_page_config(page_title="Nummer ziehen", layout="wide")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }

        /* Hauptkarte – jetzt volle Breite */
        .main-card {
            background-color: #1E90FF;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 100%;
            margin-top: 20px;
            text-align: left;   /* Text linksbündig */
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

        /* BUTTON – unverändert, nur volle Breite */
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

        /* INFO BOX SICHTBAR MACHEN */
        div[data-testid="stAlert"] {
            background-color: white !important;
            color: #1E90FF !important;
            border-left: 6px solid #1E90FF !important;
            padding: 18px !important;
            font-size: 20px !important;
            margin-top: 20px !important;
        }

        div[data-testid="stAlert"] p {
            color: #1E90FF !important;
            font-size: 20px !important;
            margin: 0 !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt in voller Breite
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

    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{nummer}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Bitte warten Sie, bis Ihre Nummer aufgerufen wird.")
    st.switch_page("pages/2_Warteraum.py")
