# username="admin"
# password:123

username = input("Enter your username: ")
password = int(input("Enter your password: "))

if(username=="admin" and password==123):
    print("Login Successfull!")
elif(username!="admin"):
    print("Wrong Password")
elif(password!=123):
    print("Wrong password!")
elif(username!="admin" and password!=123):
    print("wrong username and password")
