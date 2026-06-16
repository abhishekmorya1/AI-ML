def digits(n):
    while(n>0):
        digits=n%10
        print(digits)
        n=n//10

digits(312)