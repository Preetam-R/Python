#Count frequency of elements in a list
lst = list(map(int,input("enter the numbers:").split()))
print(lst)
s = set(lst)
for i in lst:
    lst.count(i)
for j in s:
    print(f"{j} is repeated {lst.count(i)} times")

