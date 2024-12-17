import sqlite3

def init_db():
    """Initialize the database using schema.sql."""
    with sqlite3.connect("just_events.db") as conn:
        cursor = conn.cursor()
        with open("schema.sql", "r") as schema:
            cursor.executescript(schema.read())
        conn.commit()

def add_user(username, password, role, email):
    """Add a new user."""
    with sqlite3.connect("just_events.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role, email) VALUES (?, ?, ?, ?)", 
                       (username, password, role, email))
        conn.commit()

def add_vendor(name, service_type, location):
    """Add a new vendor."""
    with sqlite3.connect("just_events.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vendors (name, service_type, location) VALUES (?, ?, ?)", 
                       (name, service_type, location))
        conn.commit()

def add_event(user_id, event_type, date, location):
    """Add a new event."""
    with sqlite3.connect("just_events.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO events (user_id, event_type, date, location) VALUES (?, ?, ?, ?)", 
                       (user_id, event_type, date, location))
        conn.commit()

def get_vendors():
    """Fetch all vendors."""
    with sqlite3.connect("just_events.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, service_type, location FROM vendors")
        return cursor.fetchall()

def get_events():
    """Fetch all events."""
    with sqlite3.connect("just_events.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT event_type, date, location FROM events")
        return cursor.fetchall()
