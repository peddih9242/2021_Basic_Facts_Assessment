import random

rounds = int(input("How many questions: "))
question_count = 0
while question_count != rounds:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    question = ("{} + {}".format(x, y))
    print(question)
    user_answer = int(input("Answer: "))
    if user_answer == eval(question):
        print("Correct")
    else:
        print("Incorrect")
    question_count += 1
print("Loop done")