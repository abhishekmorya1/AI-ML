# intro

# single Inheritance
class Employee:
    start_time = "9am"
    end_time = "5pm"
    
    def changeTime(self, new_endTime):
        self.end_time = new_endTime
    
    
class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject

t1 = Teacher("maths")
t1.changeTime("9pm")

print(t1.subject, t1.start_time , t1.end_time)