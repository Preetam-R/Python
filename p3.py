# Question: Write a Python program to find the largest among three numbers entered by the user.

n1 = float(input("enter the number1:"))
n2 = float(input("enter the number2:"))
n3 = float(input("enter the number3:"))

if (n1>n2 and n1>n3):
    print(f"Number1 {n1} is greater ")
elif (n2>n1 and n2>n3):
    print(f"number 2 {n2} is greater ")
else:
    print(f"number3 {n3} is greater ")
