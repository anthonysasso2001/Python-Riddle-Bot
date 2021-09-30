# Python-Riddle-Bot
  - riddle game in Python that answers different riddles / problems through basic math algorithms, and lets you guess them if applicable...

  - solutions to how I did each module inside each of the modules, here are only basic descriptions.

  - also plan to change the license for the program because it currently says people cannot modify etc. which seems against the point for a simple python game :)

## TODO:
  - [ ] finish README by adding other riddles / problems I would like to solve
  - [ ] add some unit tests, and main menu integration tests
  - [ ] possibly look at a save / load function for 'scores' that will persist (optional and not really the point, more of a secondary goal)

## Main.py
  - Main menu for application (call this to start it)
    - main(void)
      - main menu, lets users choose which riddle / problem they would like to select or exit the application (Note* calls each option using import so code looks cleaner)

## FibonacciSequence.py
  - Fibonacci sequence functions called by menu, contains three functions
    - fibonacci(void)
      - main menu for fibonacci itself (choose calculator for the solver, guess for the game / guesser) (Note* may have issues if int gets too big haven't tested yet)

    - fibonacciGuess(void)
      - user guesses through the fibonacci sequence, until they get one wrong. Already works pretty well and due to it being fairly simple don't think I should overdo it more than it is already.

    - fibonacciCalculator(length, start)
      - calculates the sequence up to n digits (n == user inputed number)

# TO BE ADDED

## Minesweeper.py
  - Minesweeper game functions called by main, have yet to add but will port over from a C game I completed in school...

## Sudoku.py
  - Sudoku game functions I plan to add later, just placeholder for now...

## WaiterPuzzle.py
  - WaiterPuzzle game functions called by main, same as Sudoku and Minesweeper but this will be based of finding the "Ideal order" given a menu and amount to buy with. should be a bit more complex since it has multiple implementations for the sorting algorithm :)

## FindReplaceCheck.py
  - My own implimentation of a find, replace, and spell check program to help conceptualize how they work in ms word etc. Also planning on using a similar python program with regex for my bachelor's thesis (plus some prolog), but wanted to do some of the coding early and see if it's feasible. May switch to Scala instead so this might be moved into another repo if that happens...
