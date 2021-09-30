from pickle import STRING


class User:
    
    def __init__(self, inputName, inputPassword):
        self.name = inputName
        self.password = inputPassword
        self.fibonacciScore = 0
        self.minesweeperScore = 0

    def load_user_data(file_name):
        loadFile = open(file_name, "r")
        loadFile.read(self.name)
        loadFile.read(self.password)
        loadFile.read(self.fibonacciScore)
        loadFile.read(self.minesweeperScore)
    
    def save_user_data(file_name):
        saveFile = open(file_name,"w")
        saveFile.write(self.name)
        saveFile.write(self.password)
        saveFile.write(self.fibonacciScore)
        saveFile.write(self.minesweeperScore)

    def updateMScore(newScore):
        self.minesweeperScore = newScore

    def updateFScore(newScore):
        self.fibonacciScore = newScore

testFile = "testfile.pickle"
userTest:User = ("bob","testword")
userTest:User.updateMScore(10)
userTestTwo:User = ("joe","pass")
userTestTwo:User.updateFScore (20)

userTest:User.save_user_data(testFile)

userTestThree:User = User.load_user_data(testFile)
userTestFour:User = User.load_user_data(testFile)
