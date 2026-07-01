import sqlite3

DATABASE = "insightos.db"


def get_connection():
    return sqlite3.connect(DATABASE)