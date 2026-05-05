class Student:
    def __init__(self, name):
        print("Constructor Called")
        self.name = name

stud1 = Student("Abhishek") #constructor called
print(stud1.name)
