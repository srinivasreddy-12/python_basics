user_name = input("Enter user name: ") #user
password = input("Enter password: ")#pass
if user_name == "user" and password == "pass":
    print("Login sucessfull")
else:
    if user_name == "user" and password != "pass":
        print("Password is incorrect")
    else:
        print("user name is incorrect")