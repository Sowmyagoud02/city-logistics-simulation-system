import sqlite3
import os

def get_db_path():
    Base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(Base_dir)
    return os.path.join(Base_dir, "data", "deliveries.db")

def fetch_all(query, params = None):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return results