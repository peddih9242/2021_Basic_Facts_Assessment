import random

# Function(s)
def string_checker(question, valid_list, error):
    # loop function
    valid = False
    while not valid:
        # ask question and make input lowercase
        response = input(question).lower()
        # iterate through list to see if input matches
        # any valid input or first letter of valid input
        for item in valid_list:
            if response == item[0] or response == item:
                return response
        # if input does not match any items in list, print error
        else:
            print(error)

# Main routine
valid = ["addition", "subtraction", "multiplication", "division"]



# loop
a = False
while not a:
    
    # get numbers
    x = int(input("X: ")) # numbers are to be randomly generated
    y = int(input("Y: ")) # in the base component
    
    # ask if user wants to add, subtract, multiply or divide
    word = string_checker("Do you want to do addition, subtraction, multiplication or division? ", valid, "Please enter addition, subtraction, multiplication or division (or a, s, m or d).")
    if word == "a" or word == "addition":
        print("{} + {}".format(x, y))
    elif word == "s" or word == "subtraction":
        print("{} - {}".format(x, y))
    elif word == "m" or word == "multiplication":
        print("{} * {}".format(x, y))
    elif word == "d" or word == "division":
        print("{} / {}".format(x, y))