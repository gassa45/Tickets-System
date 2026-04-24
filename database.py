import psycopg2
import os

# ---------------------------------------------------------
# Verbindung zu Supabase Postgres (Connection Pooler)
# ---------------------------------------------------------

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "6543")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode="require"
    )

# ---------------------------------------------------------
# Datenbank initialisieren
# ---------------------------------------------------------

def init_db():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    id SERIAL PRIMARY KEY,
                    nummer VARCHAR(10) NOT NULL,
                    status VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()

# ---------------------------------------------------------
# Ticket erzeugen
# ---------------------------------------------------------

def create_ticket(nummer):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO tickets (nummer, status)
                VALUES (%s, 'waiting');
            """, (nummer,))
            conn.commit()

# ---------------------------------------------------------
# Aktuelles Ticket abrufen
# ---------------------------------------------------------

def get_current_ticket():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT nummer
                FROM tickets
                WHERE status = 'current'
                ORDER BY created_at DESC
                LIMIT 1;
            """)
            row = cur.fetchone()
            return row[0] if row else None

# ---------------------------------------------------------
# Wartende Tickets abrufen
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# Ticket auf "current" setzen
# ---------------------------------------------------------

def set_current_ticket(nummer):
    with get_conn() as conn:
        with conn.cursor() as cur:
            # altes current zurücksetzen
            cur.execute("""
                UPDATE tickets
                SET status = 'done'
                WHERE status = 'current';
            """)

            # neues current setzen
            cur.execute("""
                UPDATE tickets
                SET status = 'current'
                WHERE nummer = %s;
            """, (nummer,))
            conn.commit()

# ---------------------------------------------------------
# Ticket löschen
# ---------------------------------------------------------

def delete_ticket(nummer):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM tickets
                WHERE nummer = %s;
            """, (nummer,))
            conn.commit()
