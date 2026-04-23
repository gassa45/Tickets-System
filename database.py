import psycopg2
from contextlib import contextmanager

# ---------------------------------------------------------
# Supabase PostgreSQL Verbindung
# ---------------------------------------------------------

DB_CONFIG = {
    "host": "db.vzpamxbcdqzkenexoevm.supabase.co",
    "database": "postgres",
    "user": "postgres",
    "password": "Gael2012!&237",
    "port": 5432,
    "sslmode": "require"
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
