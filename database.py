import sqlite3

conn = sqlite3.connect("logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src_ip TEXT,
    dst_ip TEXT,
    protocol TEXT,
    timestamp TEXT
)
""")

def log_packet(src, dst, protocol, time):
    cursor.execute("INSERT INTO logs (src_ip, dst_ip, protocol, timestamp) VALUES (?, ?, ?, ?)",
                   (src, dst, protocol, str(time)))
    conn.commit()

def get_logs():
    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 50")
    return cursor.fetchall()