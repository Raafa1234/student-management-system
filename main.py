from database import add_student, get_students

def show_menu():
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")

def main():
    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")

            add_student(student_id, name, age, grade)

        elif option == "2":
            students = get_students()
            print("\nRegistered Students:")
            for student in students:
                print(student)

        elif option == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
