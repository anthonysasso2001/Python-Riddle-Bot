import pickle

"""
 User object for player high scores etc...
    
 :return: return user upon initalization
 :rtype: User
"""
class User(object):
    def __init__(self, name, password, fibonacciScore = 0, minesweeperScore = 0):
        
        self.name = name
        self.password = password
        self.fibonacciScore = fibonacciScore
        self.minesweeperScore = minesweeperScore

"""
    save users from list to file and truncate to 0 first, so it doesn't have duplicates
"""
def save_users(userList: list[User], fileName: str):
    with open(fileName,"wb") as outfp:
        outfp.truncate(0)
        pickle.dump(userList,outfp,pickle.HIGHEST_PROTOCOL)
    outfp.close()

"""
    load users from file into a list of users, keep going until EOF
"""
def load_users(fileName) -> list[User]:
    outputList = [User]
    with open(fileName, "rb") as infp:
        while True:
            try:
                outputList = pickle.load(infp)
            except EOFError:
                break
    infp.close()
    return outputList