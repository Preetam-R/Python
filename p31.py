#finding the key with max value from the dict
dct = {}
n = int((input("Enter the size of dictionary:")))
for i in range(n):
    key = int(input(f"Enter the {i+1} key:"))
    value = int(input(f"Enter the {i+1} value:"))
    dct[key] = value

print(dct)
maximum = max(dct.values())
print(maximum)
