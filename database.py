import logging
import sqlite3
from typing import List, Optional, Tuple

DB_NAME = "students.db"


def connect_db() -> sqlite3.Connection:
    return sqlite3.connect(DB_NAME)


def create_table() -> None:
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        """)


def add_student(student_id: int, name: str, age: Optional[int], grade: Optional[str]) -> bool:
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)",
                (student_id, name, age, grade),
            )
        return True
    except sqlite3.IntegrityError:
        logging.exception("Integrity error when adding student %s", student_id)
        return False
    except sqlite3.Error:
        logging.exception("Database error when adding student %s", student_id)
        return False


def get_students() -> List[Tuple[int, str, Optional[int], Optional[str]]]:
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, grade FROM students")
        students = cursor.fetchall()
    return students


def update_student(student_id: int, name: str, age: Optional[int], grade: Optional[str]) -> bool:
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE students
                SET name = ?, age = ?, grade = ?
                WHERE id = ?
            """,
                (name, age, grade, student_id),
            )
            updated = cursor.rowcount
        return updated > 0
    except sqlite3.Error:
        logging.exception("Database error when updating student %s", student_id)
        return False


def delete_student(student_id: int) -> bool:
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            deleted = cursor.rowcount
        return deleted > 0
    except sqlite3.Error:
        logging.exception("Database error when deleting student %s", student_id)
        return False

