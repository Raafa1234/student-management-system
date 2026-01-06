from database import add_student, get_students

def register_student(student_id, name, age, grade):
    if not student_id or not name:
        print("ID and Name are required.")
        return

    try:
        age = int(age)
    except ValueError:
        print("Age must be a number.")
        return

    add_student(student_id, name, age, grade)

def list_students():
    students = get_students()

    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Grade: {student[3]}")

from database import update_student

def modify_student(student_id, name, age, grade):
    try:
        age = int(age)
    except ValueError:
        print("Age must be a number.")
        return

    update_student(student_id, name, age, grade)
