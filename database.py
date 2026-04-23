# database.py
import psycopg2
from contextlib import contextmanager

# ---------------------------------------------------------
# PostgreSQL Konfiguration
# ---------------------------------------------------------
DB_CONFIG = {
    "host": "localhost",
    "database": "tickets",   # <-- Deine Datenbank
    "user": "postgres",
    "password": "gassa",
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
# Tabelle erstellen
# ---------------------------------------------------------
def init_db():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                nummer VARCHAR(10) NOT NULL,
                status VARCHAR(20) NOT NULL CHECK (status IN ('waiting','in_progress','done')),
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        cur.close()

# ---------------------------------------------------------
# Neues Ticket erstellen
# ---------------------------------------------------------
def create_ticket():
    with get_conn() as conn:
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM tickets;")
        count = cur.fetchone()[0] + 1

        nummer = f"A{count:03d}"

        cur.execute(
            "INSERT INTO tickets (nummer, status) VALUES (%s, %s)",
            (nummer, "waiting")
        )
        conn.commit()
        cur.close()

        return nummer

# ---------------------------------------------------------
# Wartende Tickets holen
# ---------------------------------------------------------
def get_waiting_tickets():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nummer 
            FROM tickets
            WHERE status='waiting'
            ORDER BY id;
        """)
        rows = cur.fetchall()
        cur.close()
        return [{"id": r[0], "nummer": r[1]} for r in rows]

# ---------------------------------------------------------
# Tickets in Bearbeitung holen
# ---------------------------------------------------------
def get_in_progress_tickets():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nummer 
            FROM tickets
            WHERE status='in_progress'
            ORDER BY id;
        """)
        rows = cur.fetchall()
        cur.close()
        return [{"id": r[0], "nummer": r[1]} for r in rows]

# ---------------------------------------------------------
# Nächstes Ticket aufrufen
# ---------------------------------------------------------
def call_next_ticket():
    with get_conn() as conn:
        cur = conn.cursor()

        cur.execute("""
            SELECT id, nummer 
            FROM tickets
            WHERE status='waiting'
            ORDER BY id
            LIMIT 1;
        """)
        row = cur.fetchone()

        if not row:
            cur.close()
            return None

        ticket_id, nummer = row

        cur.execute("""
            UPDATE tickets
            SET status='in_progress'
            WHERE id=%s;
        """, (ticket_id,))

        conn.commit()
        cur.close()

        return nummer

# ---------------------------------------------------------
# Ticket abschließen
# ---------------------------------------------------------
def finish_current_ticket():
    with get_conn() as conn:
        cur = conn.cursor()

        cur.execute("""
            SELECT id, nummer 
            FROM tickets
            WHERE status='in_progress'
            ORDER BY id
            LIMIT 1;
        """)
        row = cur.fetchone()

        if not row:
            cur.close()
            return None

        ticket_id, nummer = row

        cur.execute("""
            UPDATE tickets
            SET status='done'
            WHERE id=%s;
        """, (ticket_id,))

        conn.commit()
        cur.close()

        return nummer

# ---------------------------------------------------------
# Aktuelles Ticket für Warteraum
# ---------------------------------------------------------
def get_current_ticket():
    with get_conn() as conn:
        cur = conn.cursor()

        # Ticket in Bearbeitung
        cur.execute("""
            SELECT nummer 
            FROM tickets
            WHERE status='in_progress'
            ORDER BY id
            LIMIT 1;
        """)
        row = cur.fetchone()

        if row:
            cur.close()
            return row[0]

        # sonst erstes wartendes Ticket
        cur = conn.cursor()
        cur.execute("""
            SELECT nummer 
            FROM tickets
            WHERE status='waiting'
            ORDER BY id
            LIMIT 1;
        """)
        row = cur.fetchone()
        cur.close()

        return row[0] if row else "—"
