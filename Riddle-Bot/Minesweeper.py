#Minesweeper Program
#Program to run a simple minesweeper game
#By: Anthony Sasso
#Created: 2021/04/14
#Revision History
    #2021/04/14 - Started Code based off C project I did in class don't think it will transfer though so may not choose t do it
import dataclasses
#from array import *
import Random

#macros for game scores / options
EASYSIZE = 9    #got difficulties from wikipedia...
EASYMINE = 10

MEDSIZE = 16
MEDMINE = 40

HARDSIZE = 30
HARDMINE = 99

MAXINPUT = 30
MINE = -2
UNINIT = -1

@dataclasses
class User:
    name: str
    password: str
    fibonacciScore: int = 0
    minesweeperScore: int = 0
class MBoard:
    rows: int
    columns: int

    numOfMines: int
    currentMines: int = 0

    currentBoard = []
    filledBoard = []

def initalizeBoard(inputWidth,inputHeight,inputMineNum):
    outputBoard = MBoard(inputWidth,inputHeight,inputMineNum)

    for row in range (outputBoard.rows + 2):  #+2 is for buffer around board
        for col in range(outputBoard.columns + 2):
            outputBoard.currentBoard.append(UNINIT)
            outputBoard.filledBoard.append(UNINIT)
    # print (outputBoard.currentBoard)
    # print("\n")
    # print (outputBoard.filledBoard)
    mineRow:int = 0
    mineColumn:int = 0
    while (outputBoard.currentMines < outputBoard.numOfMines):
        mineRow = Random.randrange(1,outputBoard.rows)
        mineColumn = Random.randrange(1,outputBoard.columns)
        if (MINE != (outputBoard.filledBoard[mineRow][mineColumn] and mineRow != 0 and mineColumn != 0)):
            outputBoard.filledBoard[mineRow][mineColumn] = MINE
            outputBoard.currentMines += int(1)

		# 		    x-1		    x			 x+1
				 
		# y-1		[x-1][y-1]	[x][y-1]	[x+1][y-1]

		# y		    [x-1][y]	[x][y]		[x+1][y]

		# y+1		[x-1][y+1]	[x][y+1]	[x+1][y+1]

    #calculates the amount of mines surrounding the position using virtualization above
    for row in range(1, outputBoard.rows):
        for column in range(1, outputBoard):
            if (MINE != outputBoard.filledBoard[row][column]):
                outputBoard.filledBoard[row][column] = 0

            if (MINE != outputBoard.filledBoard[row - 1][column]):       #up
                outputBoard.filledBoard[row][column] += 1

            if (MINE != outputBoard.filledBoard[row - 1][column - 1]):   #up and left
                outputBoard.filledBoard[row][column] += 1

            if (MINE != outputBoard.filledBoard[row][column - 1]):       #left
                outputBoard.filledBoard[row][column] += 1

            if (MINE != outputBoard.filledBoard[row + 1][column - 1]):   #down and left
                outputBoard.filledBoard[row][column] += 1

            if (MINE != outputBoard.filledBoard[row + 1][column]):       #down
                outputBoard.filledBoard[row][column] += 1

            if (MINE != outputBoard.filledBoard[row + 1][column + 1]):   #down and right
                outputBoard.filledBoard[row][column] += 1

            if (MINE != outputBoard.filledBoard[row][column + 1]):       #right
                outputBoard.filledBoard[row][column] += 1

            if (MINE != outputBoard.filledBoard[row - 1][column + 1]):   #up adn right
                outputBoard.filledBoard[row][column] += 1

    return outputBoard

def printCurrentBoard(printBoard:MBoard):
    
    for i in range(0,printBoard.columns):
        if (0 == i):
            print("[-]\t")
        else:
            print("[{}]\t",i)
    print("\n\n")
    for row in range(1,printBoard.rows):
        for column in range (1, printBoard.columns):
            if (UNINIT == printBoard.currentBoard[row][column]):
                print("[?]\t")
            else:
                print("[{}]\t",printBoard.currentBoard[row][column])
        print("\n\n")
    print("\n\n")
    return

def printFinalBoard(printBoard:MBoard):
    
    for i in range(0,printBoard.columns):
        if (0 == i):
            print("[-]\t")
        else:
            print("[{}]\t",i)
    print("\n\n")
    for row in range(1,printBoard.rows):
        for column in range (1, printBoard.columns):
            if (MINE == printBoard.currentBoard[row][column]):
                print("[M]\t")
            elif (UNINIT == printBoard.currentBoard[row][column]):
                print("[?]\t")
            # elif(0 == printBoard.currentBoard[row][column]):
            #     print("[0]\t")
            else:
                print("[{}]\t",printBoard.currentBoard[row][column])
        print("\n\n")
    print("\n\n")
    return

def checkInput(inputBoard:MBoard,inputRow,inputColumn):
    if (MINE == inputBoard.filledBoard[inputRow][inputColumn]):
        return 1
    elif (UNINIT == inputBoard.filledBoard[inputRow][inputColumn]):
        return 2
    else:
        return 0
def checkWin(inputBoard):
    for row in range(1,inputBoard.rows):
        for col in range(1, inputBoard.columns):
            if((inputBoard.currentBoard[row][col] != inputBoard.filledBoard[row][col]) and (MINE != inputBoard.filledBoard[row][col])):
                return False
    return True

def updateBoard(gameBoard):
    inputRow:int = 0
    inputColumn:int = 0
    print("Please enter a coordinate\n")
    print("ROW #: ")
    inputRow = input('')
    print("COLUMN #: ")
    inputColumn = input('')
    if (-1 == inputRow or -1 == inputColumn):
        return 3
    checkValue = checkInput(gameBoard,inputRow,inputColumn)
    if (0 > inputRow or inputRow > gameBoard.rows or 0 > inputColumn or inputColumn > gameBoard.columns):
        print("oops, that coordinate is off the board!\n")
        return 0 #not worth ending, just go back to select
    if (0 == checkValue):
        gameBoard.currentBoard[inputRow][inputColumn] = gameBoard.filledBoard[inputRow][inputColumn]
        win:bool = checkWin(gameBoard)
        if (True == win):
            return 2
        else:
            return 0
    elif (1 == checkValue):
        return 1#hit a mine!!!
    elif (2 == checkValue):
        print("spot already selected...\n")
        win:bool == checkWin(gameBoard)
        if (True == win):
            return 2
        else:
            return 0
    else:
        print("ERROR: failed to update Board")
        exit(2)
    return

def playerLose(gameBoard):
    print("Oh no you lost!\n")
    print("The board you had was:\n\n")
    printCurrentBoard(gameBoard)
    print("The full board was:\n\n")
    printFinalBoard(gameBoard)
    return

def playerWin(inputUser,newScore):
    print("Congratulations, you win!\n")
    if (inputUser.minesweeperScore < newScore):
        inputUser.minesweeperScore = newScore
        print("You beat your high score, your new high score is {}",newScore)

def minesweeperStart(inputUser):
    print("Enter one of the following options (case sensitive)\n")
    print("EASY - Width 09, Height 09, 10 mines\n")
    print("MEDIUM - Width 16, Height 16, 40 mines\n")
    print("HARD - Width 16, Height 30, 99 mines\n")
    print("CUSTOM - (up to max of) Width 30, Height 60, 1000 mines\n")
    loop = True
    inputWidth = 0
    inputHeight = 0
    inputMineNum = 0
    
    while (True == loop):
        print("\nNew Game selected, choose a difficulty:")
        difficultyChoice = input('')
        if ('EASY' == difficultyChoice):
            print("Easy chosen\n")
            inputWidth = EASYSIZE
            inputHeight = EASYSIZE
            inputMineNum = EASYMINE
            loop = False

        elif('MEDIUM' == difficultyChoice):
            print("Medium chosen")
            inputWidth = MEDSIZE
            inputHeight = MEDSIZE
            inputMineNum = MEDMINE
            loop = False

        elif('HARD' == difficultyChoice):
            print("Hard chosen")
            inputWidth = HARDSIZE
            inputHeight = HARDSIZE
            inputMineNum = HARDMINE
            loop = False

        elif('CUSTOM' == difficultyChoice):
            print("Custom chosen")
            print("Input width (max of 30):")
            inputWidth = input('')

            print("Input height (max of 60):")
            inputHeight = input('')

            print("Input number of mines (max of 1000 or width * height):")
            inputMineNum = input('')
            if ((0 < inputWidth <= 30) and (0 < inputHeight <= 60) and (0 < inputMineNum <= 1000) and (inputMineNum < (inputWidth * inputHeight))):
                loop = False
            else:
                print("incorrect range of input")

        else:
            print("Unknown input, try again...\n")
    #difficulty select over, now to init
    gameBoard:MBoard = initalizeBoard(inputWidth,inputHeight,inputMineNum)
    continueGame = int(0)
    while(0 == continueGame):
        printCurrentBoard(gameBoard)
        continueGame = updateBoard(gameBoard)

    if (1 == continueGame):
        playerLose(gameBoard)
    elif (2 == continueGame):
        score = int(gameBoard.numOfMines * (gameBoard.rows * gameBoard.columns))
        playerWin(inputUser,score)

    return

def minesweeperRules():
    print("The rules are:\n\n")
    print("1. The number on a spot tells you the amount of mines surrounding it from 1-8\n")
    print("2. The game ends if you select a spot with a mine\n")
    print("3. The goal is to uncover all the spaces OTHER than the ones with mines, and finish the game\n")
    print("Note* This game does not have a time limit so take your time and think it over\n\n")
    return

def minesweeper():
    inputUser = User('testName','testPassword',10,10)#just for testing until main passes user into it...
    loop = True
    while(True == loop):
        print("welcome to minesweeper\n")
        print("Current highscore = {}",inputUser)
        print("Enter \'Start\' to guess the sequence, \'Rules\' to view the rules, and \'Halt\' to exit\n")
        choice = input('')

        if (('Start' or 'start') == choice):
            minesweeperStart(inputUser)
        elif (('Rules' or 'rules') == choice):
            minesweeperRules()
        elif (('Halt' or 'halt') == choice):
            loop = False
        else:
            print("unkown input, try again...\n")
    return