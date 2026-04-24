# app.py
import streamlit as st
from database import init_db



st.set_page_config(page_title="Ticket-System", page_icon="🎫")

# Sidebar blau
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1E90FF;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Globales Styling
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .ticket-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            margin-top: 15px;
        }
        .ticket-number {
            font-size: 70px;
            font-weight: bold;
            color: #1E90FF;
        }
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

# DB nur EINMAL initialisieren
if "db_initialized" not in st.session_state:
    try:
        init_db()
    except Exception as e:
        st.error(f"Datenbankfehler: {e}")

st.title("🎫 Ticket-System mit Supabase und Streamlit")
st.write("Wähle links: Kunden, Warteraum oder Sachbearbeiter.")
