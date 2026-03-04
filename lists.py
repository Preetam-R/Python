
marks = [20.6, 45.6, 99, 23.6, 83.5]
print(marks)
print(type(marks))
print(marks[2])
print(marks[0])

#lists are mutable unlike strings and tuples

lst = ["Preetam", 19, "Bijapur", 99.4]
print(lst[0])
print(lst[3])
print(len(lst))
print(lst)

lst[2] = "Banglore"
print(lst)
lst.insert(2,143)    #insert operation needs to be specify positon and value
lst.append(20)       #whereas append operation directly asks for value adds value at end 
print(lst)

#like string we can also use slicling
#lets's create new list

car = ["BMW", "Porsche", "Audi", "Mercedes", "Toyota", "Mahindra"]

print(car[3:6])  #we can have negative index too

values = [22, 44, 33, 1, 32, 23]
values.sort()  #sorts in ascending order
print(values)  
values.sort(reverse = True)  #sorts in decending order
print(values)

#sorting also works on strings if u ave stored in your lists

car.sort()
print(car)
car.sort(reverse = True)
print(car)

marks.reverse() #yeh puri value ko palat deta hai
print(marks)