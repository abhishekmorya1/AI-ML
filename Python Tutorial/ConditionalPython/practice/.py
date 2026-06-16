# count vowels

word = "abhishek"
count=0

for i in word:
    if(i == 'a' or i == 'e' or i == 'i' or i=='o' or i=='u'):
        count+=1

print("The count of vowel is: ", count)