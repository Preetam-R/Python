#check wheather the data given by user is palindrome or not
list = []
el1 = input("Enter the 1st element of palindrome ")
list.append(el1)
el2 = input("Enter the 2nd element of palindrome ")
list.append(el2)
el3 = input("Enter the 3rd element of palindrome ")
list.append(el3)
el4 = input("Enter the 4th element of palindrome ")
list.append(el4)
el5 = input("Enter the 5th element of palindrome ")
list.append(el5)

print("the given list are:",list)

copy_list = list.copy()

copy_list.reverse()

if(list == copy_list):
    print("this is palindrome")
else:
    print("its not palindrome")




