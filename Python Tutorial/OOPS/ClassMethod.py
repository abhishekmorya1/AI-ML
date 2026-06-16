class Student:
    School_name = "ABC School"

    @classmethod
    def new_school(cls, new_name):
        cls.School_name = new_name
    

print(Student.School_name) #print old school name

Student.new_school("XYZ School")
print(Student.School_name)  #print new school name