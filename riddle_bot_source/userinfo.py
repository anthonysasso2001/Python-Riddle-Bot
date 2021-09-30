from _typeshed import Self
from dataclasses import dataclass
import pickle

@dataclass
class User:
    """Class for user struct / class"""
    name: str = "-1"
    password: str = "-1"
    fibonacciScore: int = 0
    minesweeperScore: int = 0
    
    def load_user_data(file_name):
        open(file_name, "r")
        try:
            Self = pickle.load(file_name)
        except:
            Self = []
    
    def save_user_data(file_name):
        open(file_name,"wb")
        pickle.dump(Self, file_name)

    
