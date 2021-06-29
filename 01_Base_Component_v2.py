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

# number checker, makes sure that answers are valid and checks
# that the rounds are valid (checks for infinite mode)
def num_check(question, error):
    valid = False
    while not valid:
        try:
            # ask for input
            response = int(input(question))
            # if input is negative, print error
            if response < 0:
                print(error)
                print()
            else:
                return response
        # if answer is not an integer, print error
        except ValueError:
            print(error)
            print()


# instruction function, prints instructions
def instructions():
    print()
    statement_gen("INSTRUCTIONS", "*")
    print("- First,  we'll ask you which difficulty you'd like to play. The options are easy, medium and hard.")
    print("- Next, you'll give us the amount of questions that you'd like to answer. You can choose to go"
          " into infinite mode by giving me 0.")
    print("- Once the game has been set up, you'll be asked math questions which you will need to answer.")
    print("- The game ends either when you've run out of questions, or when you use the exit code '12345' to end the"
          " game.")
    print("- Once the game has ended, we'll show you your stats and rate your performance out of 5 stars, "
          "1 being the worst score and 5 being the best.")


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


# heading for game
statement_gen("Maths Quiz", "?")
print()

# ask if user has played before and give instructions if they haven't
played_before = string_checker("Have you played this game before? ", yes_no, "Please enter yes or no (or y / n).")
if played_before == "no":
    instructions()
print()

# loop the game
loop_game = ""
while loop_game == "":
    # reset round history every game
    round_history = []
    # get the number of rounds (or take in <blank> for infinite mode)
    questions = num_check("How many questions would you like to play? (or give me 0 for infinite mode): ", "Please type an integer that is 0 or higher (give me 0 to activate infinite mode).")
    print()
    # ask for the difficulty the user wants to play
    statement_gen("Difficulties", "!")
    print()
    difficulty = string_checker("Would you like to play easy, medium or hard? ", diffs, "Please enter easy, medium or hard.")
    print()

    # based on difficulty set the operations that can be chosen
    # and the higher boundary of the numbers in the questions
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

    # loop each question and set up round variables
    loop_question = False
    questions_done = 0
    questions_correct = 0
    questions_incorrect = 0
    while not loop_question:
        questions_done += 1
        # print heading each question
        if questions == 0:
            statement_gen("Infinite Mode - Question {}".format(questions_done), "*")
        else:
            statement_gen("Question {} of {}".format(questions_done, questions), "*")
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

        # only check for multiplication and division if it is one of the two
        if operation_chosen >= 3:

            # generate numbers for multiplication and division
            x = random.randint(1, high_num_multi)
            y = random.randint(1, high_num_multi)

            # if multiplication chosen, get multiplication question
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
        # ask the user for their answer and remind user every 5 rounds that they can use
        # the exit code to stop the game at any time
        if questions_done % 5 == 0:
            print("Reminder: Enter '12345' as your answer to exit the game!")
        print("Question: {}".format(problem))
        user_answer = num_check("Answer: ", "Please enter an integer that is 0 or above.")

        # end the game if exit code given (don't allow if no questions answered)
        if user_answer == 12345:
            questions_done -= 1
            if questions_done == 0:
                print("Please answer a question before exiting!")
                print()
            else:
                loop_question = True

        # check if the user was correct/incorrect and tell user
        elif user_answer == answer:
            print("Correct!")
            questions_correct += 1
            result = "Question {}: You said {} = {:.0f} which is correct!".format(questions_done, problem, user_answer)
            round_history.append(result)
            print()
        else:
            print("Incorrect, the answer was {:.0f}.".format(answer))
            questions_incorrect += 1
            result = "Question {}: You said {} = {:.0f} which is incorrect, the answer was {:.0f}."\
                .format(questions_done, problem, user_answer, answer)
            round_history.append(result)
            print()

        # end the game if completed the amount of questions given
        if questions_done != 0:
            if questions_done == questions:
                loop_question = True

    # print game stats and amount of questions correct/incorrect
    print()
    statement_gen("Game Summary", "*")
    print()
    statement_gen("Correct: {} | Incorrect: {}".format(questions_correct, questions_incorrect), "=")
    print()

    # calculate rating and show rating to user
    # 100-81% of questions correct = 5 stars, 80-61% = 4 stars,
    # 60-41% = 3 stars, 40-21% = 2 stars, 20-0% = 1 star

    average = 1 / questions_done * questions_correct

    if 1 >= average > 0.8:
        statement_gen("Your Performance: *****", "!")
    elif 0.8 >= average > 0.6:
        statement_gen("Your Performance: ****", "!")
    elif 0.6 >= average > 0.4:
        statement_gen("Your Performance: ***", "!")
    elif 0.4 >= average > 0.2:
        statement_gen("Your Performance: **", "!")
    elif 0.2 >= average >= 0:
        statement_gen("Your Performance: *", "!")
    print()

    # ask if user wants to see round history
    show_rounds = input("Press <enter> to see your round history or any key to move on: ")
    if show_rounds == "":
        print()
        for item in round_history:
            print(item)
    print()
    # ask if user wants to keep playing, if not then end loop
    loop_game = input("Press <enter> to keep going or any key to quit: ")
    print()
# thank user for playing when program ends
print("Thanks for playing.")
