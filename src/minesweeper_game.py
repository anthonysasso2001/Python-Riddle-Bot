#Minesweeper Program
#Program to run a simple minesweeper game
#By: Anthony Sasso
#Created: 2021/04/14

#from array import *
import random
from userinfo import User
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

class _minesweeper_board:
    rows: int
    columns: int

    numOfMines: int
    currentMines: int = 0

    currentBoard = [[]]
    filledBoard = [[]]
    def __init__(self,inputWidth:int,inputHeight:int,inputMineNum:int):
        self.rows = inputWidth
        self.columns = inputHeight
        self.numOfMines = inputMineNum

        for row in range (0,(self.rows + 2)):  #+2 is for buffer around board
            self.currentBoard.append([])
            self.filledBoard.append([])
            for col in range(self.columns + 2):
                self.currentBoard[row].append(UNINIT)
                self.filledBoard[row].append(UNINIT)
                if (0>col):
                    print("ERROR: collumn allocation exception")
                    exit(1)
        # print (self.currentBoard)
        # print("\n")
        # print (self.filledBoard)
        mineRow:int = 0
        mineColumn:int = 0
        while (self.currentMines < self.numOfMines):
            mineRow = random.randint(1,(self.rows))
            mineColumn = random.randint(1,(self.columns))
            if (MINE != int(self.filledBoard[mineRow][mineColumn])):
                self.filledBoard[mineRow][mineColumn] = MINE
                self.currentMines += int(1)

            # 		    x-1		    x			 x+1
                    
            # y-1		[x-1][y-1]	[x][y-1]	[x+1][y-1]

            # y		    [x-1][y]	[x][y]		[x+1][y]

            # y+1		[x-1][y+1]	[x][y+1]	[x+1][y+1]

        #calculates the amount of mines surrounding the position using virtualization above
        for row in range(1, self.rows):
            for column in range(1, self.columns):
                if (MINE != self.filledBoard[row][column]): #only check on spaces that are not mines
                    self.filledBoard[row][column] = 0

                    if (MINE == self.filledBoard[row - 1][column]):       #up
                        self.filledBoard[row][column] += 1

                    if (MINE == self.filledBoard[row - 1][column - 1]):   #up and left
                        self.filledBoard[row][column] += 1

                    if (MINE == self.filledBoard[row][column - 1]):       #left
                        self.filledBoard[row][column] += 1

                    if (MINE == self.filledBoard[row + 1][column - 1]):   #down and left
                        self.filledBoard[row][column] += 1

                    if (MINE == self.filledBoard[row + 1][column]):       #down
                        self.filledBoard[row][column] += 1

                    if (MINE == self.filledBoard[row + 1][column + 1]):   #down and right
                        self.filledBoard[row][column] += 1

                    if (MINE == self.filledBoard[row][column + 1]):       #right
                        self.filledBoard[row][column] += 1

                    if (MINE == self.filledBoard[row - 1][column + 1]):   #up adn right
                        self.filledBoard[row][column] += 1
                    
    def print_current_board(self):
        for i in range(0, self.columns+1):
            if (0 == i):
                print('[-]\t',end='')
            else:
                print('[{0}]\t'.format(i),end='')
        print("\n\n")
        for row in range(1, self.rows+1):
            print("[{0}]\t".format(row),end='')
            for column in range (1, self.columns+1):
                if (UNINIT == self.currentBoard[row][column]):
                    print('[?]\t',end='')
                else:
                    print('[{0}]\t'.format(self.currentBoard[row][column]),end='')
            print("\n\n")
        print("\n\n")
        return

    def print_final_board(self):
        for i in range(0,self.columns+1):
            if (0 == i):
                print('[-]\t',end='')
            else:
                print('[{0}]\t'.format(i),end='')
        print("\n\n")
        for row in range(1,self.rows+1):
            print("[{0}]\t".format(row),end='')
            for column in range (1, self.columns+1):
                if (MINE == self.filledBoard[row][column]):
                    print('[M]\t',end='')
                elif (UNINIT == self.filledBoard[row][column]):
                    print('[?]\t',end='')
                # elif(0 == printBoard.currentBoard[row][column]):
                #     print("[0]\t")
                else:
                    print('[{0}]\t'.format(self.filledBoard[row][column]),end='')
            print("\n\n")
        print("\n\n")
        return

    def update_board(self,inputRow:int,inputColumn:int):
        # inputRow:int = 0
        # inputColumn:int = 0
        # print("Please enter a coordinate\n")
        # print("ROW #: ")
        # inputRow = input('')
        # print("COLUMN #: ")
        # inputColumn = input('')
        
        if ((-1 == inputRow) or (-1 == inputColumn)):
            return 3
        checkValue = check_input(self,inputRow,inputColumn)
        if (0 > inputRow or inputRow > self.rows or 0 > inputColumn or inputColumn > self.columns):
            print("oops, that coordinate is off the board!\n")
            return 0 #not worth ending, just go back to select
        if (0 == checkValue):
            self.currentBoard[inputRow][inputColumn] = self.filledBoard[inputRow][inputColumn]
            win:bool = check_win(self)
            if (True == win):
                return 2
            else:
                return 0
        elif (1 == checkValue):
            return 1#hit a mine!!!
        elif (2 == checkValue):
            print("spot already selected...\n")
            win:bool == check_win(self)
            if (True == win):
                return 2
            else:
                return 0
        else:
            print("ERROR: failed to update Board")
            exit(2)
        return

def check_input(inputBoard:_minesweeper_board, inputRow:int, inputColumn:int):
    filled_position = (inputBoard.filledBoard[inputRow][inputColumn])
    if (MINE == filled_position):
        return 1
    elif (UNINIT == filled_position):
        return 2
    else:
        return 0
        
def check_win(inputBoard:_minesweeper_board):
    for row in range(1,inputBoard.rows+1):
        for col in range(1, inputBoard.columns+1):
            if(((inputBoard.currentBoard[row][col]) != (inputBoard.filledBoard[row][col])) and (MINE != (inputBoard.filledBoard[row][col]))):
                return False
    return True

def player_lose(gameBoard:_minesweeper_board):
    print("Oh no you lost!\n")
    print("The board you had was:\n\n")
    gameBoard.print_current_board()
    print("The full board was:\n\n")
    gameBoard.print_final_board()
    return

def player_win(inputUser:User,newScore:int):
    print("Congratulations, you win!\n")
    if (inputUser.minesweeperScore < newScore):
        inputUser.minesweeperScore = newScore
        print("You beat your high score, your new high score is {0}".format(newScore))

def minesweeper_start(inputUser:User):
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
            inputWidth = int(input())

            print("Input height (max of 60):")
            inputHeight = int(input())

            print("Input number of mines (max of 1000 or width * height):")
            inputMineNum = int(input())
            if ((0 < inputWidth <= 30) and (0 < inputHeight <= 60) and (0 < inputMineNum <= 1000) and (inputMineNum < (inputWidth * inputHeight))):
                loop = False
            else:
                print("incorrect range of input")

        else:
            print("Unknown input, try again...\n")
    #difficulty select over, now to init
    gameBoard = _minesweeper_board(inputWidth,inputHeight,inputMineNum)
    continueGame = int(0)
    while(0 == continueGame):
        gameBoard.print_current_board()
        guessRow = 0
        guessColumn = 0
        print("Please enter a coordinate\n")
        print("ROW #: ")
        guessRow = int(input(''))
        print("COLUMN #: ")
        guessColumn = int(input(''))
        continueGame = gameBoard.update_board(guessRow,guessColumn)

    if (1 == continueGame):
        player_lose(gameBoard)
    elif (2 == continueGame):
        score = int(gameBoard.numOfMines * (gameBoard.rows * gameBoard.columns))
        player_win(inputUser,score)
    elif (3 == continueGame):
        print("Game Ended, final board was:\n\n")
        gameBoard.print_final_board()

    return

def minesweeper_rules():
    print("The rules are:\n\n")
    print("1. The number on a spot tells you the amount of mines surrounding it from 1-8\n")
    print("2. The game ends if you select a spot with a mine\n")
    print("3. The goal is to uncover all the spaces OTHER than the ones with mines, and finish the game\n")
    print("Note* This game does not have a time limit so take your time and think it over\n\n")
    return

def run_minesweeper():
    inputUser = User('testName','testPassword',10,10)#just for testing until main passes user into it...
    loop = True
    while(True == loop):
        print("welcome to minesweeper\n")
        print("Current highscore = {0}".format(inputUser.minesweeperScore))
        print("Enter \'Start\' to guess the sequence, \'Rules\' to view the rules, and \'Halt\' to exit\n")
        choice = input('')

        if (('Start' or 'start') == choice):
            minesweeper_start(inputUser)
        elif (('Rules' or 'rules') == choice):
            minesweeper_rules()
        elif (('Halt' or 'halt') == choice):
            loop = False
            return inputUser
        else:
            print("unkown input, try again...\n")
    return