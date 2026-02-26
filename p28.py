#covert the given list pf characters into capitalize

lst = list(input("Enter the words:").split())

print(lst)
result = []
for i in range(len(lst)):
    result.append(lst[i].capitalize())

print("the capitalized list is:",result)