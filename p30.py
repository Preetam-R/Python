#Count frequency of characters in a string
st = input("Enter the string:")
lst = list(st)
dct = {}
for i in lst:
    key = i
    value = lst.count(i)
    dct[key] = value
for i in dct:
    print(f"\n{i} --> {dct[i]}")

    
