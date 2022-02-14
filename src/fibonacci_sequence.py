#Fibonacci Sequence Program
#Program to solve fibonacci sequence, and lets user go through it for fun
#By: Anthony Sasso
#Created: 2021/02/20

def fibonacci_guess():
    play = True #first always initalizes
    inputNum = 0
    loopNum = 0
    while play:
        print("how many do you think you can guess? (enter a number below 0 at any time to exit)")
        loopNum = int(input("I can guess: "))

        if 0 > loopNum: #in case of instant exit, or exit after playing x times
            play = False

        i = 0 #resets if loop repeats

        for i in range(loopNum+1): #beginnig of guessing game

            if 0 > i:   #exit option
                play = False
                i = loopNum

            elif 0 == i:   #first needs to be 0...
                fibNumN = 0
                inputNum = int(input("number {0}\t: ".format(i)))
                if 0 == inputNum:
                    play = True
                    win = True
                else:
                    play = False
                    win = False
                    i = loopNum

            elif 1 == i:   #first needs to be 0...
                fibNumN = 1
                inputNum = int(input("number {0}\t: ".format(i)))

                if (1 == inputNum):
                    play = True
                    win = True
                    fibNum1 = 1
                    fibNum2 = 0

                else:
                    play = False
                    win = False
                    i = loopNum

            else:   #calculates number if correct calculates next and continues
                fibNumN = (fibNum1 + fibNum2)
                inputNum = int(input("number {0}\t: ".format(i)))

                if (inputNum == fibNumN):
                    fibNum2 = fibNum1
                    fibNum1 = fibNumN
                    win = True
                    play = True
                    #continue loop...
                else:
                    play = False    #exits loop
                    win = False
                    i = loopNum

        if True == win:
            print("Congratulations, you win!")

        else:
            print("Oh no you are incorrect the correct answer was: {0}".format(fibNumN))
    return

def fibonacci_calculator(length, start):
    for i in range(start, length+1):
        if 0 > i:   #cannot be below 0...
            print("ERROR: start below 0")
            return

        elif 0 == i:   #if its == 0 print 0
            print("{0} = 0".format(i))

        elif 1 == i:   #if its == 0 print 0
            print("{0} = 1".format(i))
            fibNum1 = 1#sets variables for math part
            fibNum2 = 0
        else:   #else calculate number based off F(n-1) + F(n-2)
            fibNumN = (fibNum1 + fibNum2)
            print("{0} = {1}".format(i,fibNumN))
            fibNum2 = fibNum1
            fibNum1 = fibNumN
    print("\n")
    return

def run_fibonacci(): #"main" for this algorithm called by menu module
    print("inside fibonacci sequence\n")
    print("Enter \"Guess\" to guess the sequence, \"Show\" to calculate the sequence, and \"Exit\" to exit\n")
    choice = input("")
    guessOption = {"Guess","guess"}
    showOption = {"Show","show"}
    exitOption = ("Exit", "exit")

    if choice in guessOption:
        fibonacci_guess()

    elif choice in showOption:
        length = int(input("enter the sequence length: "))
        start = 0
        fibonacci_calculator(length,start)

    elif choice in exitOption:
        return
