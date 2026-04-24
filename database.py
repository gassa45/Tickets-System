import psycopg2
from contextlib import contextmanager
import streamlit as st



# ---------------------------------------------------------
# Supabase PostgreSQL Verbindung
# ---------------------------------------------------------

DB_CONFIG = {
    "host": "aws-0-eu-west-1.pooler.supabase.com",
    "database": "postgres",
    "user": "postgres.vzpamxbcdqzkenexoevm",
    "password": "gassayossa2012",
    "port": 5432,
    "sslmode": "require",
    "sslrootcert": "system"
}


# ---------------------------------------------------------
# Verbindung als Context-Manager
# ---------------------------------------------------------
@contextmanager
def get_conn():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()

# ---------------------------------------------------------
# Tabelle erstellen (falls nicht vorhanden)
# ---------------------------------------------------------
def init_db():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                nummer VARCHAR(10),
                status VARCHAR(20),
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()

if "db_initialized" not in st.session_state:
    try:
        init_db()
        st.session_state["db_initialized"] = True
    except Exception as e:
        st.error("Fehler bei der Datenbankverbindung.")
