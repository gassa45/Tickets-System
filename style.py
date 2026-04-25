import streamlit as st
import os

def load_logo_top():
    # Absoluter Pfad zum Logo (funktioniert für /pages und Hauptordner)
    logo_path = os.path.join(os.path.dirname(__file__), "revolution.png")

    # CSS für rundes Logo
    st.markdown("""
    <style>
    .logo-round {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Logo anzeigen (zentriert)
    st.markdown(
        f'<img src="revolution.png" class="logo-round">',
        unsafe_allow_html=True
    )
