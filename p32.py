#using 2 list create a dictionary
n = int(input("Enter the size of the list:"))
dct = {}
lst = []
se = set()
for i in range(n):
    key = input(f"Enter the {i+1} key:")
    se.add(key)
for j in range(n):
    value = input(f"Enter the {j+1} value:")
    lst.append(value)

dct = dict(zip(se,lst))

print("Final dictionary is",dct)