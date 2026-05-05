info = {
    ("Abhishek", "Math"),
    ("Karan", "Science"),
    ("Abhishek", "Science"),
    ("Himanshu", "Math"),
    ("Kunal", "Math"),
    ("Abhishek" , "English"),
    ("Himanshu", "English")
}

courses_Set = set()

# using for loop print every tuple

for tup in info:
    # print(tup[0])
    # print(tup[1])
    courses_Set.add(tup[1]) #courses

print(courses_Set)


for name,course in info:
    print(name, course)

for name, course in info:
    if(course == "English"):
        print(name)
