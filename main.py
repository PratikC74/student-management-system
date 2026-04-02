from manager import StudentManager


def menu():
    print("\n🎓 Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    manager = StudentManager()

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = input("Enter ID: ").strip()
            name = input("Enter name: ").strip()
            grade = input("Enter Grade: ").strip()
            manager.add_student(student_id, name, grade)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            student_id = input("Enter ID to update: ").strip()
            name = input("Enter new Name: ").strip()
            grade = input("Enter new Grade: ").strip()
            manager.update_student(student_id, name, grade)

        elif choice == "4":
            student_id = input("Enter ID to delete: ").strip()
            manager.delete_student(student_id)

        elif choice == "5":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()