import logging

from database import create_table
from services import modify_student, register_student, list_students, remove_student

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def show_menu():
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")


def main():
    create_table()
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == "1":
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")

            register_student(student_id, name, age, grade)

        elif option == "2":
            list_students()

        elif option == "3":
            student_id = input("Student ID to update: ")
            name = input("New name: ")
            age = input("New age: ")
            grade = input("New grade: ")

            modify_student(student_id, name, age, grade)

        elif option == "4":
            student_id = input("Student ID to delete: ")
            remove_student(student_id)

        elif option == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
