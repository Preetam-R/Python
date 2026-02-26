digits = input("enter the digits:")

lst = list(digits)
print(lst)

re = input("enter the digit you want to replace:")
re1 = input("entr the digits you want to replace with in list:")

for i in range(len(lst)):
    if lst[i] == re1:
        lst[i] = re
    elif lst[i] == re:
        lst[i] = re1


print(lst)
print("after replacing the digits the new number is :"," ".join(lst)) 