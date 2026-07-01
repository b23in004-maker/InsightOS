import sqlite3

connection = sqlite3.connect("insightos.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS datasets(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    dataset_name TEXT,

    rows_count INTEGER,

    columns_count INTEGER,

    quality_score REAL,

    missing_values INTEGER,

    duplicate_rows INTEGER

)
""")

connection.commit()

connection.close()

print("Database initialized successfully.")