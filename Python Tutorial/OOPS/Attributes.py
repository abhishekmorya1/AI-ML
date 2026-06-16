#class Attribute

class Student:
    name = "Abhishek" #class attribute

    def __init__(self , age, number):
        self.age =age
        self.number=number
    
    def display(self):
        print(f"Age : {self.age}, Number: {self.number}")
        

stu1 = Student(25,8700241164)
print(stu1.name)
stu1.display()



