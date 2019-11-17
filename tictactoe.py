# Define box content for the first time
boardDraw = ["1","2","3","4","5","6","7","8","9"]

# Winning Condition
winCond = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Player symbol
player = ("O","X")

# Drawing the board
def draw():
    for line in range (7):
        if line % 2 == 0:
            for col in range(3):
                print("-----", end="")
            print("")
        else:
            for col in range(3):
                if line == 1:
                    print("| "+boardDraw[col]+" |", end="")
                elif line == 3:
                    print("| "+boardDraw[col+3]+" |", end="")
                else:
                    print("| "+boardDraw[col+6]+" |", end="")
            print("")

# Check if win condition is fulfilled
def checkWin():
    win = False
    for tup1 in range(8):
        if boardDraw[winCond[tup1][0]] == boardDraw[winCond[tup1][1]] and boardDraw[winCond[tup1][0]] == boardDraw[winCond[tup1][2]]:
            win = True
            break
    return win

# Check if the box number inserted by player is not occupied
def checkBoard(testVar):
    if boardDraw[testVar - 1] not in player:
        return True
    else:
        return False

# Call this function to start the game
def startGame():
    initCheckWin = False
    draw()
    game(initCheckWin)

# The game process is here
def game(varCheckWin):
    while varCheckWin != True:
        tryLoopOne = True
        while tryLoopOne == True:
            boxPlayerOne = int(input("(Player 1 (O)) Pick a box number = "))
            boardOK = checkBoard(boxPlayerOne)
            if boardOK == False:
                print("The selected box is not empty. Try again.")
            else:
                tryLoopOne = False
        boardDraw[boxPlayerOne - 1] = player[0]
        draw()
        varCheckWin = checkWin()
        if varCheckWin == True:
            winPlayer = "Player 1"
            break
        tryLoopTwo = True
        while tryLoopTwo == True:
            boxPlayerTwo = int(input("(Player 2 (X)) Pick a box number = "))
            boardOK = checkBoard(boxPlayerTwo)
            if boardOK == False:
                print("The selected box is not empty. Try again.")
            else:
                tryLoopTwo = False
        boardDraw[boxPlayerTwo - 1] = player[1]
        draw()
        varCheckWin = checkWin()
        if varCheckWin == True:
            winPlayer = "Player 2"
            break
    print(winPlayer, "win!")

# Start the game
startGame()