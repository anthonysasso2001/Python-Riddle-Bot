from unicodedata import name
from userinfo import *

def settings_menu(userList: list[User]):
    settingsLoop = True
    while (settingsLoop):
        print("Enter a setting option by name, or number")
        print("1 \"create user\"\n")
        print("2 \"delete user\"\n")
        print("3 \"clear save\"\n")
        print("enter \"-1\" or \"exit\" to exit\n")
        userInput = input(": ")
        createOption = {"1","create user"}
        deleteOption = {"2","delete user"}
        clearOption = {"3","clear save"}
        exitOption = {"-1","exit"}
        if userInput in createOption:  #create user initalizer
            createLoop = True
            while(createLoop):
                print("Creating new user...\n\n")

                print("Enter the username")
                userName = input(": ")

                print("Enter the password")
                userPass = input(": ")

                newUser:User = User(userName,userPass)  #add info for user then append to list

                print("adding user to list...\n")
                userList.append(newUser)

                print("Add another user, or exit back to settings menu?")
                print("y \"create another user\"\n")
                print("n \"return to menu\"\n")
                userChoice = input(": ")
                if (("y" or "create another user") == userChoice):
                    createLoop = True #redundant but just put it here in case...
                elif(("n" or "return to menu") == userChoice):
                    createLoop = False
                else:
                    print("Unknown input, please try again\n\n")

        elif userInput in deleteOption:    #delete user initalizer
            deleteLoop = True
            while(deleteLoop):
                print("Enter the username of the user you want to delete")
                userName = input(": ")

                print("Enter the password for that user")
                userPass = input(": ")
                newUser:User = User(userName,userPass)

                for user in userList:
                    if userName == user.name:
                        if userPass == user.password:
                            userList.remove(user)
                        else:
                            print("incorrect password for user")
                
                print("Add another user, or exit back to settings menu?")
                print("y \"delete another user\"\n")
                print("n \"return to menu\"\n")
                userChoice = input(": ")
                if (("y" or "delete another user") == userChoice):
                    deleteLoop = True #redundant but just put it here in case...
                elif(("n" or "return to menu") == userChoice):
                    deleteLoop = False
                else:
                    print("Unknown input, please try again\n\n")

        elif userInput in clearOption:    #clear save initalizer
            clearLoop = True
            while(clearLoop):
                print("Are you sure you want to clear your save? [y/n]\n") #test to see if it enters
                print("[all data will be deleted...\n")
                userChoice = input(": ")

                if (("y") == userChoice):
                    clearLoop = False
                    userList.clear()
                    print("All save data deleted...\n\n")
                elif(("n") == userChoice):
                    clearLoop = False
                else:
                    print("Unknown input, please try again\n\n")

        elif userInput in exitOption:    #end initalizer
            settingsLoop = False

        else:
            print("Unknown input, please try again\n")