CGPA = float(input("Enter your CGPA:"))
passed = input("Did you pass the exam(yes/no):")
is_eligible = (CGPA>=7.5 and passed=="yes")
print("Is the student eligible for the scholarship:",is_eligible)