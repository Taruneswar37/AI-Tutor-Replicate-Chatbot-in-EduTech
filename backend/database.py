import sqlite3

def test_db():
    conn = sqlite3.connect("data/metadata.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS media (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT
    )
    """)

    cursor.execute("INSERT INTO media (filename) VALUES ('test_audio.mp3')")
    conn.commit()

    cursor.execute("SELECT * FROM media")
    print(cursor.fetchall())

    conn.close()

if __name__ == "__main__":
    test_db()
