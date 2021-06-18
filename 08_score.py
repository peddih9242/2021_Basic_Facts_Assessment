import random

# main routine

# go through 10 rounds
rounds = 10
rounds_played = 0
rounds_won = 0
rounds_lost = 0
while rounds_played != rounds:
    rounds_played += 1
    
    # generate numbers in the question
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    problem = "{} + {}".format(x, y)
    print(problem)
    answer = int(input("Answer: "))
    if answer == eval(problem):
        print("Correct!")
        rounds_won += 1
    else:
        print("Incorrect.")
        rounds_lost += 1
print("Game Summary")
print("Correct: {} | Incorrect: {}".format(rounds_won, rounds_lost))
average = rounds_won / rounds_lost
if average > 1:
    print("Rating: ***")
elif average == 1:
    print("Rating: **")
elif average <= 1:
    print("Rating: *")