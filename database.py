import psycopg2
from contextlib import contextmanager
import streamlit as st

# ---------------------------------------------------------
# PostgreSQL Konfiguration über Streamlit Secrets
# ---------------------------------------------------------
DB_CONFIG = {
    "host": st.secrets["DB_HOST"],
    "database": st.secrets["DB_NAME"],
    "user": st.secrets["DB_USER"],
    "password": st.secrets["DB_PASSWORD"],
    "port": st.secrets["DB_PORT"],
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
                nummer VARCHAR(10) NOT NULL,
                beschreibung TEXT,
                status VARCHAR(20) NOT NULL CHECK (status IN ('waiting','in_progress','done')),
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        cur.close()

# ---------------------------------------------------------
# Neues Ticket erstellen (mit Beschreibung)
# ---------------------------------------------------------
def create_ticket(beschreibung=""):
    with get_conn() as conn:
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM tickets;")
        count = cur.fetchone()[0] + 1

        nummer = f"A{count:03d}"

        cur.execute(
            "INSERT INTO tickets (nummer, beschreibung, status) VALUES (%s, %s, %s)",
            (nummer, beschreibung, "waiting")
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
            SELECT id, nummer, beschreibung
            FROM tickets
            WHERE status='waiting'
            ORDER BY id;
        """)
        rows = cur.fetchall()
        cur.close()
        return [{"id": r[0], "nummer": r[1], "beschreibung": r[2]} for r in rows]

# ---------------------------------------------------------
# Tickets in Bearbeitung holen
# ---------------------------------------------------------
def get_in_progress_tickets():
    with get_conn() as conn:
        cur = conn.cursor()

        # 1. Alle in_progress Tickets holen
        cur.execute("""
            SELECT id, nummer, beschreibung
            FROM tickets
            WHERE status='in_progress'
            ORDER BY id;
        """)
        rows = cur.fetchall()

        # Wenn keine Tickets in_progress sind → fertig
        if not rows:
            cur.close()
            return []

        # 2. Falls MEHRERE Tickets in_progress sind → nur das erste behalten
        #    und alle anderen automatisch auf 'done' setzen
        if len(rows) > 1:
            # alle außer das erste Ticket abschließen
            for r in rows[1:]:
                cur.execute("""
                    UPDATE tickets
                    SET status='done'
                    WHERE id=%s;
                """, (r[0],))

            conn.commit()

            # nur das erste Ticket behalten
            rows = [rows[0]]

        cur.close()

        # 3. Rückgabe im gleichen Format wie vorher
        return [{"id": r[0], "nummer": r[1], "beschreibung": r[2]} for r in rows]


# ---------------------------------------------------------
# Nächstes Ticket aufrufen
# ---------------------------------------------------------
# ---------------------------------------------------------
# Nächstes Ticket aufrufen (mit Fix)
# ---------------------------------------------------------
def call_next_ticket():
    with get_conn() as conn:
        cur = conn.cursor()

        # 1. Alle bestehenden in_progress Tickets automatisch abschließen
        cur.execute("""
            UPDATE tickets
            SET status='done'
            WHERE status='in_progress';
        """)

        # 2. Nächstes waiting Ticket holen
        cur.execute("""
            SELECT id, nummer, beschreibung
            FROM tickets
            WHERE status='waiting'
            ORDER BY id
            LIMIT 1;
        """)
        row = cur.fetchone()

        if not row:
            cur.close()
            return None

        ticket_id, nummer, beschreibung = row

        # 3. Dieses Ticket auf in_progress setzen
        cur.execute("""
            UPDATE tickets
            SET status='in_progress'
            WHERE id=%s;
        """, (ticket_id,))

        conn.commit()
        cur.close()

        return {"nummer": nummer, "beschreibung": beschreibung}


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

        cur.execute("""
            SELECT nummer, beschreibung
            FROM tickets
            WHERE status='in_progress'
            ORDER BY id
            LIMIT 1;
        """)
        row = cur.fetchone()

        if row:
            cur.close()
            return {"nummer": row[0], "beschreibung": row[1]}

        cur = conn.cursor()
        cur.execute("""
            SELECT nummer, beschreibung
            FROM tickets
            WHERE status='waiting'
            ORDER BY id
            LIMIT 1;
        """)
        row = cur.fetchone()
        cur.close()

        return {"nummer": row[0], "beschreibung": row[1]} if row else None
