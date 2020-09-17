# User starts in tile (1,1)
# User should be available to move north, west, south or east until user reaches (3,1)
# User should not be available to go outside the grid
# List of moves that should not be available:
# North: while y = 3 and x,y = 2,2
# West: while x and y = 1, and x,y = 3,2
# South: while y = 1 and x,y = 2,3
# East: while x,y = 1,2, x,y = 1,3 and x,y = 2,3
# First i want to make sure that these moves cannot be made while the user hasnt won the game
# Second i want to show the user what moves are available to him at all times
# last i want to ask the user which move he wishes to make and update him of his available moves after each move until victory is reached

x,y = 1,1
while (x,y) != (3,1): # While user hasn't achieved victory, the program runs
    a = x
    b = y
    north = True # initialize all directions as available
    east = True
    south = True
    west = True
    if y == 3 or (x,y) == (2,2): # when user is in certain positions, these are the moves he cannot make
        north = False
    if (x,y) != (1,2) and (x,y) != (1,3) and (x,y) != (2,3):
        east = False
    if y == 1 or (x,y) == (2,3):
        south = False
    if y == 1 or x == 1 or (x,y) == (3,2):
        west = False

    direction = ""
    while direction == "": # Initialize the feedback of available moves to the user
        if north == True:
            direction += "(N)orth"
        elif east == True:
            direction += "(E)ast"
        elif south == True:
            direction += "(S)outh"
        elif west == True:
            direction += "(W)est"
    if east == True and direction != "(E)ast": # If user has multiple moves this adds those directions to the feedback output
        direction += " or (E)ast"
    if south == True and direction != "(S)outh":
        direction += " or (S)outh"
    if west == True and direction != "(W)est":
        direction += " or (W)est"
    print("You can travel: " + direction + ".") # Prints out which moves user can go

    directionChoice = ""
    while (x,y) == (a,b):
        directionChoice = input("Direction: ").upper() # Asks the user which move he wishes to make
        if directionChoice == "N" and north == True: # If direction he picks is a legal move, moves the coordinates accordingly
            y += 1
        elif directionChoice == "E" and east == True:
            x += 1
        elif directionChoice == "S" and south == True:
            y -= 1
        elif directionChoice == "W" and west == True:
            x -= 1
        else:
            print("Not a valid direction!") # If input is not valid, prints out error message
            print("You can travel: " + direction + ".")
print("Victory!") # Prints victory when coordinates are (3,1) 