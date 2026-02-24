#write a python program to accept the number and store it list and display it 
#in both ascending and desecending order

list = []

num = int(input("enter number of elements: "))

for i in range(num):
    n = int(input("enter the element: "))
    list.append(n)

print("The sorted list in ascending order: ")
list.sort()

print(list)

print("The sorted list in descending order: ")
list.sort(reverse=True)

print(list)

