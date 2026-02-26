#write a python program to count how many numbers are even and odd in a given list using a for loop
lst = []
j = 0
n = int(input("enter the No. of Elements:"))
for i in range(n):
    a = int(input(f"enter the {j+1} element:"))
    lst.append(a)
    j+=1


even = lst[0]
odd = lst[0]


print("The elements in the list are:",lst)
even = []
odd = []
for num in lst:
    if(num%2==0):
        even.append(num)
    if(num%2!=0):
        odd.append(num)

print(f"There are {len(even)} even numbers")
print(f"There are {len(odd)} odd numbers")


# lst = []
# n = int(input("enter the No. of Elements:"))
# for i in range(n):
#     a = int(input(f"enter the {i+1} element:"))
#     lst.append(a)
 
# even = 0
# odd = 0
# print("The elements in the list are:",lst)

# for num in lst:
#     if(num%2==0):
#         even = even + 1
#     else:
#         odd = odd + 1

# print(f"There are {even} even numbers")
# print(f"There are {odd} odd numbers")