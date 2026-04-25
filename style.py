import streamlit as st

def load_logo_top():
    # CSS für rundes Logo
    st.markdown("""
    <style>
    .logo-round {
        border-radius: 50%;
        width: 140px;
        height: 140px;
        object-fit: cover;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Logo über der Karte anzeigen
    st.markdown(
        '<img src="revolution.png" class="logo-round">',
        unsafe_allow_html=True
    )
