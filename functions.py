str="I am a coder"
first_a=str.find("a")
second_a=str.find("a",first_a+1)
print("The first occurrence of a is at index:",first_a)
print("The second occurrence of a is at index:",second_a)
new = str.replace("coder","programmer")
print(new)
print(str.endswith("er"))
print(str.capitalize())
print(str.count("a"))
print(str.find("coder"))
#write a program to find the occurence of '$' in a string
str1=input("Enter a string: ")
print(str1.count("$"))