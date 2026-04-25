import streamlit as st
from database import create_ticket

st.set_page_config(page_title="Nummer ziehen", layout="centered")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }

        /* Hauptkarte */
        .main-card {
            background-color: #1E90FF;
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 80%;
            margin: auto;
            margin-top: 60px;
            text-align: center;
        }

        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: white;
            margin-bottom: 20px;
        }

        .main-text {
            font-size: 22px;
            color: white;
            margin-bottom: 40px;
        }

        /* Ticket-Karte */
        div[data-testid="stMarkdownContainer"] .ticket-card {
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            text-align: center;
        }

        .ticket-number {
            font-size: clamp(40px, 8vw, 70px);
            font-weight: bold;
            color: #1E90FF;
        }

        /* Button */
        .stButton>button {
            background-color: #ffffff;
            color: #1E90FF;
            border-radius: 50px;
            padding: 15px 40px;
            font-size: 22px;
            font-weight: 600;
            border: none;
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            width: auto;
            min-width: 250px;
        }

        .stButton>button:hover {
            background-color: #e6e6e6;
            transform: scale(1.05);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
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
# Inhalt in Karte
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
