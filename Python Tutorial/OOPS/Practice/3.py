class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # Getter Methods
    def get_name(self):
        return self._name

    def get_roll_no(self):
        return self._roll_no

    def get_marks(self):
        return self._marks

    # Setter Methods with Validation
    def set_name(self, name):
        if name.strip() != "":
            self._name = name
        else:
            print("Name cannot be empty!")

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100!")

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative!")


# Creating an object
student1 = Student("Abhishek", 25, 85)

# Using Getter Methods
print("Name:", student1.get_name())
print("Roll No:", student1.get_roll_no())
print("Marks:", student1.get_marks())

# Using Setter Methods
student1.set_marks(90)
print("Updated Marks:", student1.get_marks())