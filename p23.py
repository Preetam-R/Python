#find the maximum and minimum numbers in list without library functions

lst = []
j = 0
n = int(input("enter the No. of Elements:"))
for i in range(n):
    a = int(input(f"enter the {j+1} element:"))
    lst.append(a)
    j+=1


max_num = lst[0]
min_num = lst[0]


print("The elements in the list are:",lst)

for num in lst:
    if(num>max_num):
        max_num=num
    if(num<min_num):
        min_num=num
            
print(f"maximum:{max_num}")
print(f"minimum:{min_num}")

        


   



       

    

