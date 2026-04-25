import streamlit as st

def load_logo():
    # CSS für rundes Logo
    st.markdown("""
    <style>
    .logo-round {
        border-radius: 50%;
        width: 130px;
        height: 130px;
        object-fit: cover;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Logo anzeigen
    st.sidebar.markdown(
        '<img src="revolution.png" class="logo-round">',
        unsafe_allow_html=True
    )
