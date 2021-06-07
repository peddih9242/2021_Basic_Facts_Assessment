def num_check(question, low=None, high=None):
    if high is not None and low is not None:
        situation = "both"
    elif high is None and low is not None:
        situation = "low only"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}.".format(low, high))
                    continue
            if situation == "low only":
                if response < low:
                    print("Please enter a number above {}.".format(low))
                    continue
            return response
        except ValueError:
            print("Please enter an integer.")