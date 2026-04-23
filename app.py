# app.py
import streamlit as st
from database import init_db

st.set_page_config(page_title="Ticket-System", page_icon="🎫")

# DB beim Start sicherstellen
init_db()

st.title("🎫 Ticket-System mit PostgreSQL")
st.write("Wähle links: Kunden, Warteraum oder Sachbearbeiter.")
