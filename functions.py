#functions and recursion
#code a python program of sum of two numbers by using function

def add(a,b):
    sum = a+b
    print(sum)

op1 = int(input("Enter the 1st operand:"))
op2 = int(input("Enter the 2nd operand:"))

add(op1,op2)
#  ypu can call the functions multiple times
#or else you can directly pass the arguments like
add(10,20)