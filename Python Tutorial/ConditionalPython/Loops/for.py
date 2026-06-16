word = "abhishek"

# iteration
for ch in word:
    print(ch)

# find something
if 'i' in word:
    print("letter exists")

# count something
count=0
for ch in word:
    if(ch == "i"):
        count+=1;

print(count)