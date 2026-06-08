import json
import os


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["age"], data["grades"])

    def __str__(self):
        return f"{self.name}, {self.age} років, середня оцінка: {self.get_average_grade():.2f}"


class StudentDatabase:
    def __init__(self, filename="students.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_student(self, student):
        students = self.read_students()
        students.append(student.to_dict())
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
        print(f"Студента {student.name} додано до бази даних.")

    def read_students(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def find_student(self, name):
        students = self.read_students()
        for student_data in students:
            if student_data["name"].lower() == name.lower():
                student = Student.from_dict(student_data)
                print(f"\nЗнайдено студента:")
                print(student)
                return student
        print(f"Студента з ім'ям '{name}' не знайдено.")
        return None

    def display_all_students(self):
        students = self.read_students()
        if not students:
            print("База даних порожня.")
            return
        print("\n=== СПИСОК СТУДЕНТІВ ===")
        for student_data in students:
            student = Student.from_dict(student_data)
            print(student)


if __name__ == "__main__":
    db = StudentDatabase()

    student1 = Student("Олександр Коваленко", 20, [90, 85, 92, 88])
    student2 = Student("Марія Шевченко", 19, [95, 98, 92, 100])
    student3 = Student("Іван Петренко", 21, [78, 82, 75, 80])

    db.add_student(student1)
    db.add_student(student2)
    db.add_student(student3)

    db.display_all_students()

    db.find_student("Марія Шевченко")
    db.find_student("Неіснуючий студент")
