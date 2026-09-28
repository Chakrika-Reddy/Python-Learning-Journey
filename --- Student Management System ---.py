# Function to add a new student
def add_student(students_list):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    student = {
        "name": name,
        "marks": marks
    }
    students_list.append(student)
    print("Student added successfully!\n")
def display_students(students_list):
    if not students_list:
        print("No students found!\n")
    else:
        print("\n--- Student List ---")
        for student in students_list:
            print(f"Name: {student['name']} | Marks: {student['marks']}")
        print()
def main():
    students_list = []
    while True:
        print("--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student(students_list)
        elif choice == '2':
            display_students(students_list)
        elif choice == '3':
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")
main()