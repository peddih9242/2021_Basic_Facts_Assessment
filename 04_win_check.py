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
                return item
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
        problem = ("{} + {}".format(x, y))
    
    elif word == "s" or word == "subtraction":
        # make sure subtraction outcome is positive
        if y > x:
            problem = ("{} - {}".format(y, x))
        else:
            problem = ("{} - {}".format(x, y))
    
    elif word == "m" or word == "multiplication":
        problem = ("{} * {}".format(x, y))
    
    elif word == "d" or word == "division":
        # make sure the outcome of division is an integer
        numerator = x * y
        # randomly choose the number to divide by
        if x % 2 == 0:
            problem = ("{} / {}".format(numerator, x))
        else:
            problem = ("{} / {}".format(numerator, y))
    print("Problem: {}".format(problem))
    answer = int(input("Answer: "))
    
    # check for correct answer
    if answer == eval(problem):
        print("Correct!")
    else:
        print("Incorrect.")