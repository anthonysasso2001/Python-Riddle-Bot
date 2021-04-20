from dataclasses import dataclass

@dataclass
class User:
    """Class for user struct / class"""
    name: str = "-1"
    password: str = "-1"
    fibonacciScore: int = 0
    minesweeperScore: int = 0