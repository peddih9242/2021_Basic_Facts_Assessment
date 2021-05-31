def string_checker(question, valid_list, error):
    valid = False
    while not valid:
        response = input(question).lower()
        for item in valid_list:
            if response == item[0] or response == item:
                return response
        else:
            print(error)

valid = ["addition", "subtraction", "multiplication", "division"]

a = False
while not a:
    word = string_checker("Do you want to do addition, subtraction, multiplication or division? ", valid, "Please enter addition, subtraction, multiplication or division (or a, s, m or d).")
    print("program continues")