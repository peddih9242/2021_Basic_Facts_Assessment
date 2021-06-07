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
operations = ["addition", "subtraction", "multiplication", "division"]

# loop
a = False
while not a:
    
    # get numbers
    x = int(input("X: ")) # numbers are to be randomly generated
    y = int(input("Y: ")) # in the base component
    
    # ask if user wants to add, subtract, multiply or divide
    word = string_checker("Do you want to do addition, subtraction, multiplication or division? ", operations, "Please enter addition, subtraction, multiplication or division (or a, s, m or d).")
    if word == "addition":
        problem = ("{} + {}".format(x, y))
    elif word == "subtraction":
        if y > x:
            problem = ("{} - {}".format(y, x))
        else:
            problem = ("{} - {}".format(x, y))
    elif word == "multiplication":
        problem = ("{} * {}".format(x, y))
    elif word == "division":
        numerator = x * y
        if x % 2 == 0:
            problem = ("{} / {}".format(numerator, y))
        else:
            problem = ("{} / {}".format(numerator, x))
    answer = eval(problem)
    if word == "d" or "division":
        improved = problem.replace("/", "÷")
    elif word == "m" or "multiplication":
        improved = problem.replace("*", "x")
    print("Problem: {}".format(improved))
    user_answer = int(input("Answer: "))
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect.")
