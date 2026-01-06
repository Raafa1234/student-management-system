import sqlite3

DB_NAME = "students.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_student(student_id, name, age, grade):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)",
        (student_id, name, age, grade)
    )

    conn.commit()
    conn.close()

    print("Student added successfully.")

def get_students():
    conn = connect_db()
    cursor = conn.cursor()

    def update_student(student_id, name, age, grade):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, grade = ?
        WHERE id = ?
    """, (name, age, grade, student_id))

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student updated successfully.")


    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return students

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted successfully.")
