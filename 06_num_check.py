import random

def answer_check():
    valid = False
    while not valid:
        try:
            response = input("Answer: ").lower()
            # if make response an integer if exit code not given
            if response != "xxx":
                response = int(response)
                return response
            # if exit code is given, exit loop
            else:
                break
        # if input is not valid, print error
        except ValueError:
            print("Please enter an integer (or the exit code).")

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

# main routine

rounds = check_rounds()
valid = False
rounds_played = 0
while not valid:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    rounds_played += 1
    if rounds == "":
        print("Infinite Mode - Round {}".format(rounds_played))
    else:
        print("Round {} of {}".format(rounds_played, rounds))
    problem = "{} + {}".format(x, y)
    print(problem)
    answer = input("Answer: ")
    if answer == "xxx":
        break
    answer = int(answer)
    if rounds_played == rounds:
        valid = True
    elif answer == eval(problem):
        print("Correct!")
    else:
        print("Incorrect.")
print("Thanks for playing")