salary = float(input("Enter the salary: "))

if(salary<30000):
    finalTaxRate= 0.05*salary
elif(salary>=30000 and salary<=70000):
    finalTaxRate = 0.15*salary
elif(salary>70000):
    finalTaxRate = 0.25*salary


print("The final tax rate is: ",finalTaxRate)