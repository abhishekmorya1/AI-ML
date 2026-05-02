
l=[1,2,3,4,5,6]

for i in l:
    print(i)

# searching in python
x=5
idx=0
for i in l:
    if(i==x):
        print(idx)
        break
    idx+=1


print(type(l))
print(len(l))