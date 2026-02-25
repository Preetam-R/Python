#code a program to find average of two numbers using functions

def avg(a,b):
    sum = a + b
    avg = sum/2
    print(avg)

n1 = int(input("Enter the 1st number"))
n2 = int(input("Enter the 2nd number"))
avg(n1,n2)

#Write a python program to print the length of the list using functions

lst = [2,4,6,77,44,1,34,6]

my = ["home","tutor","alien","VS code","College"]

def lenght(list):
    print(len(list))

lenght(my)
lenght(lst)

#to print this list lets write another function

def print_lst(list):
    for item in list:
        print(item,end=" ")

print_lst(lst)
print("\n")
print_lst(my)

#list in built keyword