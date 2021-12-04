
def CheckName(firstName):
    if "Kaloyan".lower() in firstName.lower():
        return "Yes"
    else:
        return "No"

def PrintNames(firstName, lastName):
    print("Hi my first name is "+firstName + " and my last name is "+lastName)



# if __name__ == "__main__":
firstName1 = input("What is your first name? ")
lastName1 = input("What is your last name? ")
    #PrintNames(lastNlastName=ame, firstName=firstName)
if CheckName(firstName1) == "Yes":
    PrintNames(firstName=firstName1, lastName=lastName1)
elif CheckName(firstName1) == "No":        
    print("You are not Kaloyan!!!")
else:
    print("Else")


    


