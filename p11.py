#write a program that stores the favorite movie of users and display in lists

movie1 = input("Enter your 1st movies:")

movie2 = input("Enter your 2nd movies:") 

movie3 = input("Enter your 3rd movies:") 

list = []
list.append(movie1)
list.append(movie2)
list.append(movie3)

list.sort()#to sort it in order 

print(list)



