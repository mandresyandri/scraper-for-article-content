import sqlite3

# setting the database 
def create_models():
    conn = sqlite3.connect('andri-database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scraped_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
        title_article TEXT, 
        author TEXT, 
        content TEXT
    )
    """)
    return "Database was created"

create_models()