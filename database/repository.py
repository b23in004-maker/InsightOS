import sqlite3

DATABASE = "insightos.db"


def save_dataset(dataset):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            dataset_name TEXT,
            rows_count INTEGER,
            columns_count INTEGER,
            quality_score REAL,
            missing_values INTEGER,
            duplicate_rows INTEGER

        )
    """)

    cursor.execute("""
        INSERT INTO datasets (

            dataset_name,
            rows_count,
            columns_count,
            quality_score,
            missing_values,
            duplicate_rows

        )

        VALUES (?, ?, ?, ?, ?, ?)
    """, (

        dataset["dataset_name"],
        dataset["rows"],
        dataset["columns"],
        dataset["quality_score"],
        dataset["missing_values"],
        dataset["duplicate_rows"]

    ))

    connection.commit()

    connection.close()