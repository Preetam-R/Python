#write a program to get factorial of a number

#using functions
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
num = int(input("enter the number:"))
print(factorial(num))

#without using functions
num = int(input("Enter the number: "))
fact = 1

if num < 0:
    print("Negative number can't have factorial")
elif num == 0 or num == 1:
    print("Factorial is 1")
else:
    for num in range(1, num + 1):
        fact = fact*num
    print("Factorial of", num, "is", fact)