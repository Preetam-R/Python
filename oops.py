#class and object in python
#class is a blueprint for creating an object

#creating class
class Student:
    def __init__(self,name,age,r_no):
        self.name = name
        self.age = age
        self.r_no = r_no

    def hello(self):
        print(f"Hello! {self.name} welcome to code ninjas")

                         
#Creating object(instance)

s1 = Student("Preetam",19,42)
s2 = Student("Shreenisha",18,49)
s1.hello()
s2.hello()

#we can delete enitre properties and methods
#by using del keyword 
#eg del s1

