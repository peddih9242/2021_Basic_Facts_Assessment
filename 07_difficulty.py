import random

# main routine

# ask for easy, medium or hard difficulty
difficulty = input("Easy, medium or hard? ")

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
a = False
while not a:
    
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
            problem = "{} / {}".format(numerator, x)
    print("Problem: {}".format(problem))
    answer = int(input("Answer: "))
    # check if answer is correct and tell user
    if answer == eval(problem):
        print("Correct!")
    else:
        print("Incorrect.")
