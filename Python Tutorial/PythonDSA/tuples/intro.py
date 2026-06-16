# ordered, immutable, and allow duplicates and store heterogeneous

tup = (1,2,3,4,5)

for i in tup:
    print(i)

# empty tuple

tup1 = ()
print(tup1)

# single element tuple

tup2 = (1,) #must end with , in single element tuple
print(tup2) 


#sum in tuples
tup4 = (1,2,3,4,5)
sum=0

for i in tup4:
    sum+=i

print(f"sum is: {sum}")