#Riddle-Bot
#Program to solve multiple types of riddles, acts like a menu to imported algorithms 
# By: Anthony Sasso
#Created: Feb 20, 2021
#Revision History
    #finished menu outline, fibonacci, made placeholder for future import-links

import sys
import FibonacciSequence

def main(): #main function
    loop = True
    userInput = ''
    while (loop):
        print('Enter a Riddle option by name, or number')
        print('1 \"fibonacci sequence\"\n2 \"placeholder\"\nenter \"-1\" or \"exit\" to exit\n')
        userInput = input(': ')

        if ('1' == userInput or 'fibonacci sequence' == userInput):  #fibonacci sequence initalizer
            print('picked fibonacci sequence!\n')   #test to see if it enters 
            FibonacciSequence.fibonacci()
        elif ('2' == userInput or 'placeholder' == userInput):    #placeholder initalizer
            print('picked placeholder sequence!\n') #test to see if it enters 

        elif ('-1' == userInput or 'exit' == userInput):    #placeholder initalizer
            loop = False

        else:
            print('wrong input please try again\n')
    return

main()