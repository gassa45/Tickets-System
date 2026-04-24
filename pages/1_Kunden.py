import streamlit as st
from database import create_ticket

st.set_page_config(page_title="Nummer ziehen", layout="centered")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Hintergrund */
        body {
            background-color: #f5f7fa;
        }

        /* BLAUE Karten */
        .ticket-card {
            background-color: #1E90FF;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-align: center;
            margin-top: 20px;
        }

        /* Nummer groß */
        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: white;
        }

        /* Buttons */
        .stButton>button {
            background-color: #1E90FF;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: #187bcd;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Inhalt
# ---------------------------------------------------------
st.title("🎫 Nummer ziehen")

st.write("Bitte drücken Sie auf den Button, um Ihre Wartenummer zu erhalten.")

if st.button("Nummer ziehen"):
    nummer = create_ticket()   # z.B. "A015"

    # Nummer speichern
    st.session_state["meine_nummer"] = nummer

    # Sofort weiterleiten in den Warteraum
    st.switch_page("pages/2_Warteraum.py")
