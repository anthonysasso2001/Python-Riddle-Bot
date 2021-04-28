#Riddle-Bot
#Program to solve multiple types of riddles, acts like a menu to imported algorithms
#By: Anthony Sasso
#Created: 2021/02/20
FILENAME = "saveState.txt"
from fibonacci_sequence import run_fibonacci
from minesweeper_game import run_minesweeper
from userinfo import User,save_user_data,load_user_data

def main(): #main function
    #load info
    users = load_user_data(FILENAME)


    #game menu / loop
    # loop = True
    # userInput = ''
    # while (loop):
    #     print("Enter a Riddle option by name, or number")
    #     print("1 \"fibonacci sequence\"\n")
    #     print("2 \"minesweeper\"\n")
    #     print("3 \"placeholder\"\n")
    #     print("enter \"-1\" or \"exit\" to exit\n")
    #     userInput = input(': ')
        
    #     if (('1' or 'fibonacci sequence') == userInput):  #fibonacci sequence initalizer
    #         print("picked fibonacci sequence!\n")   #test to see if it enters
    #         #current_user = run_fibonacci()
    #         run_fibonacci()
            
    #     elif (('2' or 'minesweeper') == userInput):    #minesweeper initalizer
    #         print("picked minesweeper game!\n") #test to see if it enters
    #         #current_user = run_minesweeper()
    #         run_minesweeper()

    #     elif (('3' or 'placeholder') == userInput):    #placeholder initalizer
    #         print("picked placeholder sequence!\n") #test to see if it enters

    #     elif (('-1' or 'exit') == userInput):    #placeholder initalizer
    #         loop = False

    #     else:
    #         print("wrong input please try again\n")
    #save info
    inputUserOne = User('testName','testPassword',10,10)
    inputUserTwo = User('testTwoName','secondPassword',20,20)
    inputUserThree = User('testThreeName','secondPassword',30,30)
    users:User = [inputUserOne,inputUserTwo,inputUserThree]
    save_user_data(FILENAME,users)
    return

main()