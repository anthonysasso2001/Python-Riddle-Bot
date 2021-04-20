#Riddle-Bot
#Program to solve multiple types of riddles, acts like a menu to imported algorithms
#By: Anthony Sasso
#Created: 2021/02/20

from fibonacci_sequence import run_fibonacci
from minesweeper_game import run_minesweeper
def main(): #main function
    
    loop = True
    userInput = ''
    while (loop):
        print("Enter a Riddle option by name, or number")
        print("1 \"fibonacci sequence\"\n")
        print("2 \"minesweeper\"\n")
        print("3 \"placeholder\"\n")
        print("enter \"-1\" or \"exit\" to exit\n")
        userInput = input(': ')
        
        if (('1' or 'fibonacci sequence') == userInput):  #fibonacci sequence initalizer
            print("picked fibonacci sequence!\n")   #test to see if it enters
            run_fibonacci()
            
        elif (('2' or 'minesweeper') == userInput):    #minesweeper initalizer
            print("picked minesweeper game!\n") #test to see if it enters
            run_minesweeper()

        elif (('3' or 'placeholder') == userInput):    #placeholder initalizer
            print("picked placeholder sequence!\n") #test to see if it enters

        elif (('-1' or 'exit') == userInput):    #placeholder initalizer
            loop = False

        else:
            print("wrong input please try again\n")
    return

main()