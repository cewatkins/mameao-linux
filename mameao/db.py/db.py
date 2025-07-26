import sqlite3

def get_connection(db_path):
    return sqlite3.connect(db_path)

def execute_query(conn, query, params=None):
    with conn:
        cur = conn.cursor()
        cur.execute(query, params or ())
        return cur.fetchall()
