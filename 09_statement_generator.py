def statement_gen(statement, decoration):
    # create sides to add to statement, and top / bottom decorations
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bot = decoration * len(statement)
    
    # print decorations and statements
    print(top_bot)
    print(statement)
    print(top_bot)

# main routine

valid = False
while not valid:
    state = input("Statement: ")
    decor = input("Decoration: ")
    full = statement_gen(state, decor)
    print()