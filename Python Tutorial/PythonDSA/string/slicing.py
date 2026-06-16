# slicing in string

str = "my name is abhishek morya"

print(str[11:]) #start value and default ending value (length of string)
print(str[11:20]) #start value and ending value
print(str[:20])  #default start value (0) and ending value
print(str[:len(str)]) # default start value (0) and length of string which denotes ending value
print(str[:]) # default start value (0) and default ending value (lenth of string)

# negative slicing

str1 = "python"
print(str1[-4:-2]) # negative slicing means reverse slicing
