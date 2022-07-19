# rock paper scissors game
rps (rock-paper-scissors) is a simple python project that enables users to play configurable games of rock paper scissors! The game is set by defualt to use the [rock paper scissors fire water](https://en.wikipedia.org/wiki/Rock_paper_scissors#:~:text=The%20most%20representative,this%20game.%5B104%5D) variation of the game. Note: this program was created for a culminating project; the program now serves archival purposes.

## main
The main.py file contains all logic, settings and gameplay mechanics. You can change the game by altering the main.py file. Some changes include:

- Adding moves to the moveset
- Removing moves to the moveset
- Changing the "animation" between rounds
- Changing the order in which a move beats another move (ie: paper beats rock, scissors beat paper)
- Altering the winning / losing messages 
- Changing the number of rounds

## rps
The rps.py file contains the infastructure required to create the main.py file. The rps file can be imported to other projects to easly assemble a game of rps. Player classes (ie: HumanPlayer) are inherited from the Player class 
### HumanPlayer
The human player class allows a human player to perform an action (ie: choosing rock). The action function will not allow a human player to enter an invalid move; actions are scanned with regular expression, if a player inputs an invalid move it will prompt them enter another move until they enter a valid move (if the move is contained within a mess it will count, ie: `0314scissor3431erEBr`). Once a valid move has been selected - it will be returned.
### CpuPlayer
Compared to the HumanPlayer the CpuPlayer is simple. The CpuPlayer class's action function will randomly select a valid move and return it.

### duel
The duel function returns a winner. Input both players names and the winner shall be returned (as `1` or `2`), exception: if a ties occurs `0` shall be returned. 

## Dependencies
The following are required for this program to function:

- `python 3.10`
- `re module`
- `abc module`
