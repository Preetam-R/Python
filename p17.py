#Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Your Name:")

greet = "Good Afternoon"

print(f"Hello!!",name,greet)

# Write a program to detect double space in a string.

st = input("type any sentence ")

if(st == "  "):
    print("The String has Double Space")
elif(st==" "):
    print("The string has single Space")
else:
    print("the string do not have nor single space nor double space")
