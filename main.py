 
from rps import *
from time import sleep
 
NUM_ROUNDS = 3
icons = ["🔥", "💧", "👊", "✋", "✌"] # displayed in animation
 
move_set ={ # define what move wins against what here
        "water":["fire"],
        "fire":["rock", "paper", "scissor"],
        "rock":["scissor", "water"],
        "paper":["rock", "water"],
        "scissor":["paper", "water"]
        }
 
def play_round(player1:Player, player2:Player, icons): # Only excepts Players and icons
    for icon in enumerate(icons):
        print(icon[1])
        sleep(0.5)
   
    print("Shoot!\n")
   
    move1 = player1.action(move_set) # call the action function, returns str
    move2 = player2.action(move_set)
 
    condition = duel(move1, move2, move_set)
 
    if(condition == 1): # if player 1 won
        player1.update_score() # update the score
        print(f"{player1.name} wins!")
 
    elif(condition == 2): # if player 2 won
        player2.update_score() # update the score
        print("Cpu wins!")
 
    else: # if its a tie
        print("Its a tie!")
 
human = HumanPlayer("Kaitlyn") # define human player
cpu = CpuPlayer("Cpu") # define cpu player
 
for rounds in range(NUM_ROUNDS): # repeat 3 times
    play_round(human, cpu, icons) # play a round
    print(f"\n{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
 
print("==================================================\n")
 
if(human.get_score() > cpu.get_score()): # check if the human has the most points
    print(f"{human.name} Wins!")
    print(f"{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
 
elif(cpu.get_score() < human.get_score()): # if human did not win, cpu must have won!
    print(f"{cpu.name} Wins!")
    print(f"{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
 
else: # if its a tie, no one won.
    print("The games a tie!")
    print(f"{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
 
