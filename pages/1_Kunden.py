import streamlit as st
from database import create_ticket

st.set_page_config(page_title="Nummer ziehen", layout="centered")

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

st.title("🎫 Nummer ziehen")

st.write("Bitte drücken Sie auf den Button, um Ihre Wartenummer zu erhalten.")

if st.button("Nummer ziehen"):
    nummer = create_ticket()

    st.success(f"Ihre Nummer ist: {nummer}")

    st.markdown(
        f"""
        <div class="ticket-card">
            <span class="ticket-number">{nummer}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Bitte warten Sie, bis Ihre Nummer aufgerufen wird.")
