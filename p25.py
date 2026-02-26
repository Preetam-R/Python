#write a program to get name,marks of three subject makenstore it in class find a average of three subject


class Students:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def avg(self):
        sum = self.marks1 + self.marks2 + self.marks3
        average = sum/3
        print(f"Hello!! {self.name}")
        print(f"Your average is {average:.2f}")

s1 = Students("Preetam",90,99,89)
s1.avg()
print()
s2 = Students("Shreenisha",89,98,90)
s2.avg()







