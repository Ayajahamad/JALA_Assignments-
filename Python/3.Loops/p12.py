# 12. Print gender (Male/Female) program according to given M/F using switch

def is_male():
    print("Male")

def is_female():
    print("Female")

def is_invalid():
    print("Invalid Input")

def checkGender(inp):
    check_dict={
        "M":is_male,
        "F":is_female
    }

    return check_dict.get(inp,is_invalid)()

inp = input('Enter the Gender "F" or "M" :: ')
checkGender(inp)


# Another Method

def check_Gender(gen):
    match gen:
        case "M":
            print("Male")
        case "F":
            print("Female")
        case _:
            print("Invalid Choice")

gen = input("Enter the gender :: ")
check_Gender(gen)