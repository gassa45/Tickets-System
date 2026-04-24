# app.py
import streamlit as st
from database import init_db

st.set_page_config(page_title="Ticket-System", page_icon="🎫")

# DB nur EINMAL initialisieren
if "db_initialized" not in st.session_state:
    try:
        init_db()
    except Exception as e:
        st.error(f"Datenbankfehler: {e}")

st.title("🎫 Ticket-System mit PostgreSQL")
st.write("Wähle links: Kunden, Warteraum oder Sachbearbeiter.")
