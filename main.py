from database import add_student, get_students

def main():
    print("Student Management System")

    add_student(1, "Juan Perez", 16, "11th Grade")
    add_student(2, "Maria Gomez", 17, "11th Grade")

    students = get_students()

    print("\nRegistered Students:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
