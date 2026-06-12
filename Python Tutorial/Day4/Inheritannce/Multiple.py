# multiply inheritance

class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student():
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, name, salary, gpa):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

obj1 = TA("Abhishek", 12000, "9.8")
print(obj1.name, obj1.salary, obj1.gpa )