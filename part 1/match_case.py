color = input("Enter a color: ")
match color:
    case "red":
        print("stop")
    case "yellow":
        print("look")
    case "green":
        print("go")
    case _:
        print("Wrong signal color") #default