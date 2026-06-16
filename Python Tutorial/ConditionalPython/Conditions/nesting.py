age = int(input("Enter your age: "))
has_licence = False

if(age>=18):
    if(has_licence):
        print("You can drive!")
    else:
        print("Have Licence first!")
else:
    print("You are too young!")