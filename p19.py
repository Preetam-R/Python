#  Write a program to store seven fruits in a list entered by the user.

# lst = []

i = 1

for i in range(1,8):
    fr = input(f"Enter the {i} fruit: ")
    lst.append(fr)
    lst.sort()
print(lst)

#write a multiplication table of a given number using for loop

n1 = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n1} X {i}={n1*i}")


