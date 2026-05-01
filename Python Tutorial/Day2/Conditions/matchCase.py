# just like switch

color=input("Enter the Color: ")

match color:
    case "red":
        print("Stop")
    case "green":
        print("go")
    case "orange":
        print("look")
    case _:
        print("Wrong Color!")