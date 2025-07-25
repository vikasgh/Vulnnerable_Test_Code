import sqlite3

def get_user_by_name(name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result