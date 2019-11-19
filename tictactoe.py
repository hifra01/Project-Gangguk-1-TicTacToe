# Default box content, used for game reset and move check
defaultBoard = ["1","2","3","4","5","6","7","8","9"]

# Define box content for the first time
boardDraw = ["1","2","3","4","5","6","7","8","9"]

# Winning Condition
winCond = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Player symbol
player = ("X","O")

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

# Check if there is no more move allowed
def checkMove():
    allowNextMove = False
    for i in range(9):
        if boardDraw[i] == defaultBoard[i]:
            allowNextMove = True
            break
    return allowNextMove

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

# Reset all value to default and start the game
def startGame():
    for i in range(9):
        boardDraw[i] = defaultBoard[i]
    initCheckWin = False
    draw()
    game(initCheckWin)

# The game process is here
def game(varCheckWin):
    winPlayer = ""
    while varCheckWin != True:
        tryLoopOne = True
        while tryLoopOne == True:
            boxPlayerOne = inputBoxNumber("(Player 1 (X)) Pick a box number = ")
            boardOK = checkBoard(boxPlayerOne)
            if boardOK == False:
                print("The selected box is not empty. Try again.")
            else:
                tryLoopOne = False
        boardDraw[boxPlayerOne - 1] = player[0]
        draw()
        varCheckWin = checkWin()
        if varCheckWin == True:
            winPlayer = "Player 1 win!"
            break
        nextMove = checkMove()
        if nextMove == False:
            winPlayer = "Draw, no more move are allowed"
            break
        tryLoopTwo = True
        while tryLoopTwo == True:
            boxPlayerTwo = inputBoxNumber("(Player 2 (0)) Pick a box number = ")
            boardOK = checkBoard(boxPlayerTwo)
            if boardOK == False:
                print("The selected box is not empty. Try again.")
            else:
                tryLoopTwo = False
        boardDraw[boxPlayerTwo - 1] = player[1]
        draw()
        varCheckWin = checkWin()
        if varCheckWin == True:
            winPlayer = "Player 2 win!"
            break
        nextMove = checkMove()
        if nextMove == False:
            winPlayer = "Draw, no more move are allowed"
            break
    print(winPlayer)
    gameEnd()

def gameEnd():
    playAgain = input("Do you want to play again? (y/N) ")
    if playAgain == "":
        playAgain = "N"
    if playAgain == "y" or playAgain == "Y":
        startGame()
    else:
        print("Goodbye")

# Call this function to start the game
def initGame():
    print("======== TIC-TAC-TOE ========")
    input("\n\n\nPress Enter to start the game")
    startGame()

def inputBoxNumber(name):
    boxPlayer = 0
    checkLoop = True
    while checkLoop == True:
        try:
            errValue = False
            boxPlayer = int(input(name))
        except ValueError:
            errValue = True
        if errValue == True:
            print("Please input a number")
        elif boxPlayer < 1 or boxPlayer > 9:
            print("Invalid box number. Please try again")
        else:
            checkLoop = False
    return boxPlayer

# Start the game
try:
    initGame()
except KeyboardInterrupt:
    print("\nYou just forced quit the game. Goodbye.")