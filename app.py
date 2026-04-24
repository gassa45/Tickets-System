import streamlit as st

st.set_page_config(page_title="Ticket-System", layout="centered")

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }

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
            margin-bottom: 10px;
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
        <div class="main-title">🎫 Ticket-System mit Supabase und Streamlit</div>
        <div class="main-text">Wähle links: Kunden, Warteraum oder Sachbearbeiter.</div>
    </div>
""", unsafe_allow_html=True)
