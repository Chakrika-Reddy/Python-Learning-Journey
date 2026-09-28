Name=str(input("Enter Name:"))
Course=str(input("Enter course:"))
Age=int(input("Enter Age:"))
student_profile = {
    "Name": Name,
    "Course": Course,
    "Age": Age
}
print("\n--- Student profile ---")
print("Name:",student_profile["Name"])
print("Course:",student_profile["Course"])
print("Age:",student_profile["Age"])