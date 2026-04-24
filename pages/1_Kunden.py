import streamlit as st
from database import create_ticket

st.set_page_config(page_title="Nummer ziehen", layout="centered")

st.title("🎫 Nummer ziehen")

st.write("Bitte drücken Sie auf den Button, um Ihre Wartenummer zu erhalten.")

if st.button("Nummer ziehen"):
    nummer = create_ticket()      # z.B. "A001"
    formatted = nummer            # KEINE Formatierung mehr!

    st.success(f"Ihre Nummer ist: {formatted}")

    st.markdown(
        f"""
        <div style="
            background-color:#1E90FF;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            margin-top: 20px;
        ">
            <span style="
                font-size: 70px;
                font-weight: bold;
                color: white;
            ">
                {formatted}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Bitte warten Sie, bis Ihre Nummer aufgerufen wird.")
