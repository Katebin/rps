from random import choice
import re 

def validate(action:str, action_set:dict):
    # Inorder to get the valid actions a user can use we need to grab them from the action_set dict
    # We can do this with the keys function, then converting it to a usable list
    # We also need to define "pattern" to create a regular expressions pattern later
    actions = list(action_set.keys())
    pattern = "("

    # To automaticly generate a regular expressions pattern we can use a for loop with enumerate rather than range
    # This allows us to grab the iteration and action at the same time, saving memory & time
    # We check for each iteration if it will be the last, if not we add a "|" symbol (re or indicator)
    # By using regular expressions we can easily get "scissor" from "scissors" or "paper" from "0enhpaper"
    for move in enumerate(actions):
        if(move[0] + 1 != len(actions)):
            pattern = pattern + str(move[1]) + "|" 

        else:
            pattern = pattern + str(move[1]) + ")"
    
    # We can now compile our pattern and use it to search text with re.compile()
    # Once we search the action we can check if theres a result, if the search returns "None" it does not match
    # So, we can return True if we get a result which means the action is valid
    re_pattern = re.compile(pattern)
    match = re_pattern.search(action)

    if(match != None):
        return [True, match.group(1)]
    else:
        return [False, ""]

def duel(action1:str, action2:str, action_set:dict, order=[0, 1, 2]):
    # Inorder to determine a winner we input the actions into the action_set dict
    # If the action is in the dict its a winning combo (order may change if order argument changed)
    # Once we know what wins against what we can return the winner
    if(action1 in action_set[action2]):
        return order[2]
    elif(action2 in action_set[action1]):
        return order[1]
    else:
        return order[0] # Note: 0 represents a tie

class HumanPlayer:
    def __init__(self, name:str):
        self.score = 0
        self.name = name

    def action(self, text:str, invalid_text:str, action_set):
        # To start the process of getting a user action we need to get input from the console
        # We can use the input function to achieve this
        user_action = str(input(text))
        check = validate(user_action, action_set)

        # By using the validate function previously created we can check if the input is a valid move
        # We enter the action into the functions arguments and check if it returns True
        # If it does not return True we ask the user to enter a new move, 
        # once they enter a valid move we return it

        while(check[0] != True):
            print(invalid_text)
            user_action = str(input(text))
            check = validate(user_action, action_set)

        return str(check[1])

    def update_score(self, multiplier=1):
        # Add one times the multiplier to the players score
        self.score += (1 * multiplier)

    def get_score(self):
        # Return the score of the player
        return self.score

class CpuPlayer:
    def __init__(self, name:str):
        self.score = 0
        self.name = name

    def action(self, action_set:dict):
        possible_choices = list(action_set.keys())
        cpu_choice = choice(possible_choices)

        return cpu_choice

    def update_score(self, multiplier=1):
        # Add one times the multiplier to the players score
        self.score += (1 * multiplier)

    def get_score(self):
        # Return the score of the player
        return self.score