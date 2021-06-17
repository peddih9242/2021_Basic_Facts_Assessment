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
average = 1 / rounds * rounds_won
if 1 > average >= 0.8:
    print("Rating: *****")
elif 0.8 > average >= 0.6:
    print("Rating: ****")
elif average < 0.6 or average >= 0.4:
    print("Rating: ***")
elif 0.4 > average >= 0.2:
    print("Rating: **")
elif 0.2 > average >= 0:
    print("Rating: *")