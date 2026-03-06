#while loop

# i = 1  #this is called iterator
# while(i<=5):
#     print("Preetam")
#     i = i+1  #iteration

# u = 1

# while(u<=10):
#     print(u)
#     u = u+1

# p = 10
# while(p>=0):
#     print(p)
#     p = p-1

#break and continue statement 

# li = [4, 7, 9,32,65,99,17,30]

# i = 1
# while(i<=10):
#     print(i)
#     if(i==5):
#         break
#     i = i+1
# print("end of loop")

#continue statement acts as skip in current iteration 

i = 0
while(i<=10):
    if(i==5):
        i+=1
        continue    
    print(i)
    i+=1
print("end of loop")