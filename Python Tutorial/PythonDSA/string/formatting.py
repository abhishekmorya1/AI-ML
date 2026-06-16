# string formatting can be done in two ways

#first way -> .format()

num1=5
num2=9
sum = num1 + num2
print("Sum of two number is: {}".format(sum))

print("language is: {}".format("python")) #normal formatting

print("Sum of {} and {} is {}".format(num1, num2, sum))

# we also do indexed based indexing
print("Sum of {1} and {0} is {2}".format(num1, num2, sum))

# value based formatting

print("Value of {a} and {b} is:".format(a=10,b=45))



#f-strings

a=5
b=10

print(f"sum of {a} and {b} is {a+b}")

name="Abhishek"
age = "25"
print(f"My name is {name} and my age is {age}")