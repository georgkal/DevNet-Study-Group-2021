def PrintNames(firstname, lastname):
    print("Hi my names is " +firstname + " and my last name is "+lastname)
def Checkname(firstname):
    if "Stan" in firstname:
        return True
    else:
        return False

if __name__ == "__main__":
    firstname = input("What is yourname?")
    lastname = input("What is your last name?")
    if Checkname(firstname) == True:
        PrintNames(firstname, lastname)
    elif Checkname(firstname) == False:
        print ("You are not Stan")