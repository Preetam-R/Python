#write a python program to store students details in dictionary

dct = {}
i = 0
print("enter 0 to exit")
while True:
    key = input(f"enter the {i+1} key:")
    if key == "0":
        break
    value = input(f"Enter the {i+1} value:")
    
    dct[key] = value
    i+=1
for key,value in dct.items():
    print(f"\n{key}-->{value}\n")

