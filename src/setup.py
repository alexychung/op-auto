import sqlite3

def create_sqlite_database(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print("done")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn == True:
            conn.close()

if __name__ == "__main__":
    create_sqlite_database("new.db")
