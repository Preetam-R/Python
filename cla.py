#wirte a program to find largest of 3 no. using nested if-else statement

# a = int(input("Enter the 1st number"))
# b = int(input("Enter the 2nd number"))
# c = int(input("Enter the 3rd number"))

# if(a>b and a>c):
#     print(f"{a} is greater")
# elif(b>a and b>c ):
#     print(f"{b} is greater")
# else:
#     print(f"{c} is greater")

#-------------------------------------------------------------------------------------------#

#inline if-else
# statement 1 if(condition) else statement 2

#write a above program using inline nested if-else 

# a = int(input("Enter the 1st number"))
# b = int(input("Enter the 2nd number"))
# c = int(input("Enter the 3rd number"))
# x = "a is greater" if(a>b and a>c) else ("b is greater" if(b>c and b>a) else "c  is greater")
# print(x)

#--------------------------------------------------------------------------------------------------#

#check the number is perfect square or not
# import math
# n = int(input("enter the number:"))
# sqrrt = math.sqrt(n)
# square = sqrrt*sqrrt
# if(n == square):
#     print("this is perfect square")
# else:
#     print("its not perfect square")

# #                   OR

# n = int(input("enter the number:"))
# sq = n**0.5
# sqrt = sq*sq 

# if(n == sqrt):
#     print("its perfect square number.")
# else:
#     print("its not perfect square number.")


#check whether the entered year is leap year or not 

# yr = int(input("Enter the year:"))

# if(yr % 400 == 0):
#     print("its a leap year")
# elif(yr % 4 == 0 and yr % 100 != 0):
#     print("It's a leap year")
# else:
#     print("its not leap year")

#check a number is positive, negative or zero or not
num = int(input("Enter the number:"))
if(num>0):
    print("its positive number.")
elif(num<0):
    print("its negative number.")
else:
    print("its zero")


    

