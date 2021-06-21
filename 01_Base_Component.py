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
            print()

# round checker, makes sure round input is valid and checks for infinite mode
def check_rounds():
    while True:
        # ask for amount of rounds
        response = input("How many questions would you like to play? (or <enter> for infinite mode): ")
        round_error = "Please either type an integer that is higher than 0 or press <enter> for infinite mode."
        # if user has not opted for infinite mode, 
        # make input an integer
        if response != "":
            try:
                response = int(response)
                
                # if input is too low, print an error
                if response < 1:
                    print(round_error)
                    print()
                    continue

            # if input is invalid, print an error
            except ValueError:
                print(round_error)
                print()
                continue
        return response

# number checker, makes sure that answers are valid
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

# instruction function, prints instructions
def instructions():
    print()
    statement_gen("INSTRUCTIONS", "*")
    print("- First,  we'll ask you which difficulty you'd like to play. The options are easy, medium and hard.")
    print("- Next, you'll give us the amount of questions that you'd like to answer. You can choose to go into infinite mode by pressing <enter>.")
    print("- Once the game has been set up, you'll be asked math questions which you will need to answer.")
    print("- The game ends either when you've run out of questions, or when you use the exit code '12345' to end the game.")
    print("- Once the game has ended, we'll show you your stats and rate your performance out of 5 stars, 1 being the worst score and 5 being the best.")

# statement generator, decorates important statements
def statement_gen(statement, decoration):
    # create sides to add to statement, and top / bottom decorations
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bot = decoration * len(statement)
    
    # print decorations and statements
    print(top_bot)
    print(statement)
    print(top_bot)

# Main routine
# lists for string checker valid input and game summary
diffs = ["easy", "medium", "hard"]
yes_no = ["yes", "no"]
game_summary = []

statement_gen("Maths Quiz", "?")
print()

# ask if user has played before, for amount of rounds and difficulty
played_before = string_checker("Have you played this game before? ", yes_no, "Please enter yes or no (or y / n).")
if played_before == "no":
    instructions()
print()

keep_going = ""
while keep_going == "":
    rounds = check_rounds()
    print()
    statement_gen("Difficulties", "!")
    print()
    difficulty = string_checker("Would you like to play easy, medium or hard? ", diffs, "Please enter easy, medium or hard.")
    print()

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
        if rounds == "":
            statement_gen("Infinite Mode - Question {}".format(rounds_played), "*")
        else:
            statement_gen("Question {} of {}".format(rounds_played, rounds), "*")
        print()

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
        print("Question: {}".format(problem))
        user_answer = num_check()
        
        # end the game if exit code given (don't allow if no rounds played)
        if user_answer == 12345:
            rounds_played -= 1
            if rounds_played == 0:
                print("Please answer a question before exiting!")
                print()
            else:
                valid = True

        # check if the user was correct and tell user
        elif user_answer == answer:
            print("Correct!")
            rounds_won += 1
            result = "Question {}: You said {} = {:.0f} which is correct!".format(rounds_played, problem, answer)
            game_summary.append(result)
            print()
        else:
            print("Incorrect, the answer was {}.".format(answer))
            rounds_lost += 1
            result = "Question {}: You said {} = {:.0f} which is incorrect.".format(rounds_played, problem, answer)
            game_summary.append(result)
            print()

        # end the game if rounds are done
        if rounds_played == rounds:
            valid = True

    # print game stats and rating
    statement_gen("Game Summary", "*")
    statement_gen("Correct: {} | Incorrect: {}".format(rounds_won, rounds_lost), "=")
    print()

    # calculate rating and show rating to user
    average = 1 / rounds_played * rounds_won

    if 1 >= average >= 0.8:
        print("Rating: *****")
    elif 0.8 > average >= 0.6:
        print("Rating: ****")
    elif 0.6 > average >= 0.4:
        print("Rating: ***")
    elif 0.4 > average >= 0.2:
        print("Rating: **")
    elif 0.2 > average >= 0:
        print("Rating: *")

    # ask if user wants to see round history
    show_rounds = input("Press <enter> to see your round history or any key to move on: ")
    if show_rounds == "":
        print()
        for item in game_summary:
            print(item)
    print()
    # ask if user wants to keep playing, if not then end loop
    keep_going = input("Press <enter> to keep going or any key to quit: ")
print("Thanks for playing.")