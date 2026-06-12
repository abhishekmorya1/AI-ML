# multilevel inheritance

class Employee:
    start_time = "9am"
    end_time = "5pm"

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role

class Account(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary


staff1 = Account("2500" , "CA")

print(staff1.salary , staff1.start_time, staff1.end_time, staff1.role)