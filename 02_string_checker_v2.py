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

# list with valid input
valid = ["addition", "subtraction", "multiplication", "division"]

# loop
a = False
while not a:
    # ask question for checking if function works
    word = string_checker("Do you want to do addition, subtraction, multiplication or division? ", valid, "Please enter addition, subtraction, multiplication or division (or a, s, m or d).")
    print("program continues")