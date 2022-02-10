import pickle


class User(object):
    def __init__(self, name, password, fibonacciScore, minesweeperScore):
        
        self.name = name
        self.password = password
        self.fibonacciScore = fibonacciScore
        self.minesweeperScore = minesweeperScore

def save_users(userList, fileName):
    with open(fileName,"wb") as outfp:
        pickle.dump(userList,outfp,pickle.HIGHEST_PROTOCOL)

def load_users(fileName):
    outputList = [User]
    with open(fileName, "rb") as infp:
        while True:
            try:
                outputList = pickle.load(infp)
            except EOFError:
                break
    return outputList
