import logging
from typing import Optional

from database import add_student, delete_student, get_students, update_student


def register_student(student_id: str, name: str, age: str, grade: Optional[str]) -> None:
    if not student_id or not name:
        print("ID and Name are required.")
        return

    try:
        sid = int(student_id)
    except ValueError:
        print("Student ID must be an integer.")
        return

    try:
        age_val = int(age) if age != "" else None
    except ValueError:
        print("Age must be a number.")
        return

    success = add_student(sid, name.strip(), age_val, grade.strip() if grade else None)
    if success:
        print("Student added successfully.")
    else:
        print("Failed to add student (maybe duplicate ID).")


def list_students() -> None:
    students = get_students()
    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Grade: {student[3]}")


def modify_student(student_id: str, name: str, age: str, grade: Optional[str]) -> None:
    try:
        sid = int(student_id)
    except ValueError:
        print("Student ID must be an integer.")
        return

    try:
        age_val = int(age) if age != "" else None
    except ValueError:
        print("Age must be a number.")
        return

    success = update_student(sid, name.strip(), age_val, grade.strip() if grade else None)
    if success:
        print("Student updated successfully.")
    else:
        print("Student not found or update failed.")


def remove_student(student_id: str) -> None:
    try:
        sid = int(student_id)
    except ValueError:
        print("Student ID must be an integer.")
        return

    success = delete_student(sid)
    if success:
        print("Student deleted successfully.")
    else:
        print("Student not found or delete failed.")
