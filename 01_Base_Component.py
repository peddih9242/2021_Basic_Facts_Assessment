import random

# Functions

# string checker, checks for valid input from a list
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

# round checker, makes sure round input is okay and checks for
# infinite mode
def check_rounds():
    while True:
        # ask for amount of rounds
        response = input("How many rounds: ")
        round_error = "Please type either an integer that is higher than 0."
        # if user has not opted for infinite mode, 
        # make input an integer
        if response != "":
            try:
                response = int(response)
                
                # if input is too low, print an error
                if response < 1:
                    print(round_error)
                    continue

            # if input is invalid, print an error
            except ValueError:
                print(round_error)
                continue
        return response

# number checker, makes sure that the answer is valid
def num_check():
    valid = False
    while not valid:
        try:
            # ask for answer
            response = int(input("Answer: "))
            # if given answer is negative, print error
            if response < 0:
                print("Please enter an integer above 0.")
            else:
                return response
        # if answer is not an integer, print error
        except ValueError:
            print("Please enter an integer.")

# Main routine
# lists for string checker valid input
operations = ["addition", "subtraction", "multiplication", "division"]
diffs = ["easy", "medium", "hard"]

# ask for how many rounds
rounds = check_rounds()

# ask if user wants to add, subtract, multiply or divide
word = string_checker("Do you want to do addition, subtraction, multiplication or division? ", operations, "Please enter addition, subtraction, multiplication or division (or a, s, m or d).")

# loop
valid = False
rounds_played = 0

# ask for difficulty and set difficulty based on response
difficulty = string_checker("Which difficulty would you like to play (easy / medium / hard): " , diffs, "Please enter easy, medium or hard.")
if difficulty == "easy":
    low_num = 1
    high_num = 5
elif difficulty == "medium":
    low_num = 3
    high_num = 10
elif difficulty == "hard":
    low_num = 5
    high_num = 15
while not valid:
    rounds_played += 1
    # get numbers to use in equation
    x = random.randint(low_num, high_num)
    y = random.randint(low_num, high_num)

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
        problem = ("{} / {}".format(numerator, y))
    answer = eval(problem)
    if word == "d" or "division":
        improved = problem.replace("/", "÷")
    elif word == "m" or "multiplication":
        improved = problem.replace("*", "x")
    print("Problem: {}".format(improved))
    user_answer = num_check()
    if answer == 12345 or rounds_played == rounds:
        valid = True
    elif user_answer == eval(problem):
        print("Correct!")
    else:
        print("Incorrect.")
