import streamlit as st

def load_logo_top():
    st.markdown(
        """
        <div style="text-align:center; margin-bottom:20px;">
            <img src="../revolution.png" width="180">
        </div>
        """,
        unsafe_allow_html=True
    )
