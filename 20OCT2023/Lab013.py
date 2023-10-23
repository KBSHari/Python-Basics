
name=input("Enter your name:\n")

match name:
    case "KBS":
        print("Verified user")
    case "Hari":
        print(" Partically verified user")
    case _:
        print("Not verified user")