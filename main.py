 
from rps import *
from time import sleep
 
NUM_ROUNDS = 3
icons = ["🔥", "💧", "👊", "✋", "✌"]
 
move_set ={
        "water":["fire"],
        "fire":["rock", "paper", "scissor"],
        "rock":["scissor", "water"],
        "paper":["rock", "water"],
        "scissor":["paper", "water"]
        }
 
def play_round(player1:Player, player2:Player, icons):
    for icon in enumerate(icons):
        print(icon[1])
        sleep(0.5)
   
    print("Shoot!\n")
   
    move1 = player1.action(move_set)
    move2 = player2.action(move_set)
 
    condition = duel(move1, move2, move_set)
 
    if(condition == 1):
        player1.update_score()
        print(f"{player1.name} wins!")
 
    elif(condition == 2):
        player2.update_score()
        print("Cpu wins!")
 
    else:
        print("Its a tie!")
 
human = HumanPlayer("Kaitlyn")
cpu = CpuPlayer("Cpu")
 
for rounds in range(NUM_ROUNDS): # repeat 3 times
    play_round(human, cpu, icons) # play a round
    print(f"\n{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
 
print("==================================================\n")
 
if(human.get_score() > cpu.get_score()): # check if the human won
    print(f"{human.name} Wins!")
    print(f"{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
 
elif(cpu.get_score() > human.get_score()): # if human did not win, cpu must have won!
    print(f"{cpu.name} Wins!")
    print(f"{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
 
else:
    print("The games a tie!")
    print(f"{human.name} score: {human.get_score()}\t{cpu.name} score: {cpu.get_score()}") # display the score
