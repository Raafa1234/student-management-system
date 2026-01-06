students = []

def add_student(student_id, name, age, grade):
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    print("Student added successfully.")

def get_students():
    return students
