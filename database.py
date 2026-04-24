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
}


# ---------------------------------------------------------
# Verbindung als Context-Manager
# ---------------------------------------------------------
@contextmanager
def get_conn():
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"],
        sslmode="require",
        sslrootcert=None  # wichtig: None = Systemzertifikate
    )
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
        st.error(f"Datenbankfehler: {e}")

def create_ticket():
    with get_conn() as conn:
        with conn.cursor() as cur:
            # Neue Ticketnummer erzeugen (höchste Nummer + 1)
            cur.execute("SELECT COALESCE(MAX(CAST(nummer AS INTEGER)), 0) + 1 FROM tickets;")
            neue_nummer = cur.fetchone()[0]

            # Ticket einfügen
            cur.execute("""
                INSERT INTO tickets (nummer, status)
                VALUES (%s, %s)
                RETURNING nummer;
            """, (str(neue_nummer), "waiting"))

            ticket_nummer = cur.fetchone()[0]
            conn.commit()
            return ticket_nummer

def get_current_ticket():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT nummer 
                FROM tickets
                WHERE status = 'in_progress'
                ORDER BY created_at ASC
                LIMIT 1;
            """)
            row = cur.fetchone()
            return row[0] if row else None

def get_waiting_tickets():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT nummer
                FROM tickets
                WHERE status = 'waiting'
                ORDER BY created_at ASC;
            """)
            rows = cur.fetchall()
            return [r[0] for r in rows]
