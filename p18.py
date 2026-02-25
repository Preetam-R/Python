#create a list and print the elements of the list using for loop

# li = [1,8,4,90,1211,56,17,30]

# for el in li:
#     print(el)

#make a tuple and search any element in tuple

# tup = (4,6,7,22,33,96,)

# for val in tup:
    
#     if(val==22):
#         print("element found",val)
#         break
#     else:
#         print("element not found")
        
#     print(val)

#print the numbers from 1 to 100 using for and range 

for i in range(1,101):
    print(i)


#print the numbers from 100 to 1 using for and range 
for x in range(100,0,-1):
    print(x)

#take a input from the user and print the table of n number

n = int(input("enter the number to print table: "))
for i in range(1,11):
    print(n,"X",i,"=",n*i)

#print the sum of first n natural numbers
n = int(input("Enter the natural number"))
sum = 0
for i in range(n):
    sum+=i
print(f"the total sum of first",n,"natural number is ", sum)

#find the factorial of n number 

n = int(input("Enter the number"))
fact = 1
for i in range(n):
    fact+=i
print(fact)

        
