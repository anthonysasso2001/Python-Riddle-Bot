#Riddle-Bot
#Program to solve multiple types of riddles, acts like a menu to imported algorithms
#By: Anthony Sasso
#Created: 2021/02/20
FILENAME = "resources/saveState.pkl"
import re

from fibonacci_sequence import run_fibonacci
from minesweeper_game import run_minesweeper
from userinfo import *
from settings import settings_menu


def main(): #main function
    #load info
    userList = load_users(FILENAME)

    #game menu / loop
    loop = True
    while (loop):
        print("Enter a Riddle option by name, or number")
        print("1 \"fibonacci sequence\"\n")
        print("2 \"minesweeper\"\n")
        # print("3 \"placeholder\"\n")
        print("enter \"0\" or \"settings\" for settings\n")
        print("enter \"-1\" or \"exit\" to exit\n")
        userInput = input(": ")
        firstOption = {"1","fibonacci sequence"}
        secondOption = {"2","minesweeper"}
        settingOption = {"0","settings"}
        exitOption = {"-1","exit"}

        if userInput in firstOption:  #fibonacci sequence initalizer
            print("picked fibonacci sequence!\n")   #test to see if it enters
            #current_user = run_fibonacci()
            run_fibonacci()
            
        elif userInput in secondOption:    #minesweeper initalizer
            print("picked minesweeper game!\n") #test to see if it enters
            #current_user = run_minesweeper()
            run_minesweeper()

        # elif (("3" or "placeholder") == userInput):    #placeholder initalizer
        #     print("picked placeholder sequence!\n") #test to see if it enters
        
        elif userInput in settingOption:    #settings initalizer
            print("entering settings\n") #test to see if it enters
            settings_menu(userList)

        elif userInput in exitOption:    #end initalizer
            loop = False

        else:
            print("Unknown input, please try again\n")
    
    #save info
    save_users(userList,FILENAME)
    return

main()