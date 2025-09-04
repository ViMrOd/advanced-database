import sqlite3

conn = sqlite3.connect("my_super_fun_database.db") #or :memory for temp stuff

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    name TEXT        
)
""")

conn.commit()