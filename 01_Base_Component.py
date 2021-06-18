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
        response = input("How many questions would you like to play? (or <enter> for infinite mode): ")
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

def instructions():
    print("INSTRUCTIONS")
    print("you choose difficulty")
    print("you choose rounds")
    print("you get question")
    print("you answer right or wrong we tell you")
    print("we rate performance at end")
    
# Main routine
# lists for string checker valid input and game summary
diffs = ["easy", "medium", "hard"]
game_summary = []

# ask for how many questions the user wants to play
rounds = check_rounds()

# ask for easy, medium or hard difficulty
difficulty = string_checker("Easy, medium or hard? ", diffs, "Please enter easy, medium or hard.")

# based on difficulty set the operations that can be chosen
# and the higher boundary of the numbers in the question
if difficulty == "easy":
    high_num_add = 10
    op_high = 2
elif difficulty == "medium":
    high_num_add = 20
    high_num_multi = 5
    op_high = 3
elif difficulty == "hard":
    high_num_add = 50
    high_num_multi = 10
    op_high = 4

# loop the game and set up round variables
valid = False
rounds_played = 0
rounds_won = 0
rounds_lost = 0
while not valid:
    rounds_played += 1

    # choose which operation to go through, 1 is addition
    # 2 is subtraction, 3 is multiplication, 4 is division
    operation_chosen = random.randint(1, op_high)
    
    # generate numbers for addition / subtraction
    x = random.randint(1, high_num_add)
    y = random.randint(1, high_num_add)

    # if addition chosen, get addition question
    if operation_chosen == 1:
        problem = "{} + {}".format(x, y)

    # if subtraction chosen, get subtraction question
    elif operation_chosen == 2:
        # make sure that the result of subtraction is positive
        if y > x:
            problem = "{} - {}".format(y, x)
        else:
            problem = "{} - {}".format(x, y)
    if operation_chosen >= 3:
        # generate numbers for multiplication and division
        x = random.randint(1, high_num_multi)
        y = random.randint(1, high_num_multi)
        
        # if multiplication chosen, get multiplcation question
        if operation_chosen == 3:
            problem = "{} * {}".format(x, y)
        
        # if division chosen, get division question
        elif operation_chosen == 4:
            numerator = x * y
            problem = "{} / {}".format(numerator, y)
    
    # get answer of the question
    answer = eval(problem)

    # change the look of the question to be more understandable
    if operation_chosen == 3:
        problem = problem.replace("*", "x")
    elif operation_chosen == 4:
        problem = problem.replace("/", "÷")
    print("Problem: {}".format(problem))
    user_answer = num_check()
    if answer == 12345 or rounds_played == rounds:
        valid = True

    # check if the user was correct and tell user
    elif user_answer == answer:
        print("Correct!")
        rounds_won += 1
        result = "Round {}: You said {} = {} which is correct!".format(rounds_played, problem, answer)
        game_summary.append(result)
    else:
        print("Incorrect.")
        rounds_lost += 1
        result = "Round {}: You said {} = {} which is incorrect.".format(rounds_played, problem, answer)
        game_summary.append(result)
print("Game Summary")
print("Correct: {} | Incorrect: {}".format(rounds_won, rounds_lost))
average = 1 / rounds * rounds_won
if 1 > average >= 0.8:
    print("Rating: *****")
elif 0.8 > average >= 0.6:
    print("Rating: ****")
elif 0.6 > average >= 0.4:
    print("Rating: ***")
elif 0.4 > average >= 0.2:
    print("Rating: **")
elif 0.2 > average >= 0:
    print("Rating: *")
show_rounds = input("Show each round? ")
if show_rounds == "yes":
    for item in game_summary:
        print(item)
else:
    print("Thanks for playing")