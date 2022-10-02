import sqlite3

# setting the database 
def create_models():
    conn = sqlite3.connect('andri-database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scraped_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
        title TEXT, 
        author TEXT, 
        date_update TEXT,
        image TEXT,
        content TEXT
    )
    """)
    conn.commit()
    return "Database was created"

create_models()