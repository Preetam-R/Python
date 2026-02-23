#table of number
n = int(input("Enter the number:"))
if(n==0):
    print("Anything multipiled by zero is zero")
else:
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)


