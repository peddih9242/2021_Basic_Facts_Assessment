def string_checker(question):
    valid = False
    while not valid:
        # take in response and make sure it's lowercase
        response = input(question).lower()
        # check for valid input, if none then print an error
        if response == "a" or response == "addition":
            print("program continues")
            return "addition"
        elif response == "s" or response == "subtraction":
            print("program continues")
            return "subtraction"
        elif response == "m" or response == "multiplication":
            print("program continues")
            return "multiplication"
        elif response == "d" or response == "division":
            print("program continues")
            return "division"
        else:
            print("Please enter addition / subtraction / multiplcation / division.")

# main routine

loop = False
while not loop:
    operation = string_checker("Would you like to do addition, subtraction, multiplication or division? ")
