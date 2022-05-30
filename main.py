import rps

def main():
    moves = {"water":["fire"], "fire":["rock", "paper", "scissor"], "rock":["scissor"], "paper": ["rock"], "scissor": ["paper"]}
    player1 = rps.HumanPlayer("Kaitlyn")
    player2 = rps.HumanPlayer("Cpu")

    p1_move = player1.action("user >>", "Invalid please try again", moves)
    p2_move = player2.action("user >>", "Invalid please try again", moves)

    print(rps.duel(p1_move, p2_move, moves))

if(__name__ == "__main__"):
    main()