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

def store_candidate_details(name, email, phone, experience, position, location, tech_stack):
    conn = sqlite3.connect("talentmate.db")  # Connect to database
    cursor = conn.cursor()

    # Insert candidate data
    cursor.execute('''
        INSERT INTO candidates (full_name, email, phone, experience, position, location, tech_stack)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, experience, position, location, tech_stack))

    conn.commit()
    candidate_id = cursor.lastrowid  # Get the ID of the inserted candidate
    conn.close()

    return candidate_id

def get_all_candidates():
    conn = sqlite3.connect("talentmate.db")
    cursor = conn.cursor()

    # Fetch all candidates
    candidates = cursor.execute("SELECT id, full_name, position, tech_stack FROM candidates").fetchall()
    conn.close()

    return candidates

def store_responses(candidate_id, questions_list, responses):
    conn = sqlite3.connect("talentmate.db")  # Connect to database
    cursor = conn.cursor()

    for i, question in enumerate(questions_list, start=1):
        answer = responses.get(i, "")  # Get answer, default to empty string if not found
        
        cursor.execute(
            "INSERT INTO responses (candidate_id, question, answer) VALUES (?, ?, ?)",
            (candidate_id, question, answer),
        )

    conn.commit()  # Save changes
    conn.close()  # Close database connection

def return_responses(candidate_id):
    conn = sqlite3.connect("talentmate.db")
    cursor = conn.cursor()

    # Using parameterized query to prevent SQL injection
    query = "SELECT * FROM responses WHERE candidate_id = ?"
    cursor.execute(query, (candidate_id,))
    
    # Fetch all matching responses
    result = cursor.fetchall()

    conn.close()
    return result

if __name__ == "__main__":
    init_database()
    print("Database initialized Successfully")