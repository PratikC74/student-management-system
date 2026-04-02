import json
import os
from student import Student

class StudentManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student_id, name, grade):
        for student in self.students:
            if student["id"] == student_id:
                print("❌ Student ID already exists!")
                return

        new_student = Student(student_id, name, grade)
        self.students.append(new_student.to_dict())
        self.save_students()
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("📭 No student records found.")
            return

        print("\n📋 Student List:")
        print("-" * 40)
        for s in self.students:
            print(f"ID: {s['id']} | Name: {s['name']} | Grade: {s['grade']}")
        print("-" * 40)

    def update_student(self, student_id, name, grade):
        found = False

        for student in self.students:
            if student.get("id") == student_id:
                student["name"] = name
                student["grade"] = grade
                found = True
                break

        if found:
            self.save_students()
            print("✅ Student updated successfully!")
        else:
            print("❌ Student not found!")
    

    def delete_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                self.save_students()
                print("🗑️ Student deleted successfully!")
                return

        print("❌ Student not found!")