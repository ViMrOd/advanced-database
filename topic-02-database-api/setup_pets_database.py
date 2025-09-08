import sqlite3

conn = sqlite3.connect("pets.db")

cursor = conn.cursor()

try:
    cursor.execute("""
        DROP TABLE users
    """)
except:
    pass

cursor.execute("""
    CREATE TABLE pet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        kind TEXT,
        noise TEXT
    )
""")


pet_data  
cursor.execute("""
    INSERT INTO pet (name, kind)
    VALUES ("dorothy", "dog")
""")

conn.commit()




