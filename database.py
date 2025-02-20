import sqlite3

def init_database():
    conn = sqlite3.connect("talentmate.db")
    cursor = conn.cursor()

    # Table for storing candidate details
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email TEXT,
            phone TEXT,
            experience INTEGER,
            position TEXT,
            location TEXT,
            tech_stack TEXT
        )
    ''')

    # Table for storing chatbot interactions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_id INTEGER,
            question TEXT,
            answer TEXT,
            FOREIGN KEY (candidate_id) REFERENCES candidates(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    print("Database initialized Successfully")