list1 = input("Enter list elements separated by spaces: ").split()
list2 = input("Enter list elements separated by spaces: ").split()
copy_list1 = list1.copy()
copy_list2 = list2.copy()
copy_list1.reverse()
copy_list2.reverse()
if copy_list1 == list1:
    print("list1 is palindrome")
else:
    print("list1 is not palindrome")
if copy_list2 == list2:
    print("list2 is palindrome")
else:
    print("list2 is not palindrome")