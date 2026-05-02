# list creations

marks = [23,45,34,56,64]
print(marks)

# list can store heterogeneous datatypes

list1 = [1,2,"abhishek",3.23,[32,4,3]]
print(list1)

# list are mutable in nature means we can modify the list
marks[2]=100
print(marks)

# list contain duplicates

list2 = [1,2,1,2,1,2]
print(list2)

# slicing in lists same as slicing in strings
print("Slicing Part Start")
slice1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


print(slice1[11:]) #start value and default ending value (length of string)
print(slice1[11:20]) #start value and ending value
print(slice1[:20])  #default start value (0) and ending value
print(slice1[:len(slice1)]) # default start value (0) and length of string which denotes ending value
print(slice1[:]) # default start value (0) and default ending value (lenth of string)

# negative slicing
print(slice1[-4:-2]) # negative slicing means reverse slicing
