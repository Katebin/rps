 
from abc import abstractmethod
from random import choice
import re
 
def validate(action:str, action_set:dict):
    # Regular expressions remove noise before & after a keyword, making it easier to get the correct action.
    # This builds a regular expression that will match the valid actions, then tests the input with the regular expression
 
    # Inorder to get the valid actions a user can use we need to grab them from the action_set dict
    # We can do this with the keys function, then converting it to a usable list
    actions = list(action_set.keys())
 
    # We also need to define "pattern" to create a regular expressions pattern later
    # To automatically generate a regular expressions pattern we can use the join function to generate a pattern
    pattern = "("+"|".join(actions) + ")"
 
    # ↓↓↓ The pattern above is the short way to do this ↓↓↓
    """
    pattern = "("
 
    for move in enumerate(actions):
        if(move[0] + 1 != len(actions)):
            pattern = pattern + str(move[1]) + "|"
 
        else:
            pattern = pattern + str(move[1]) + ")"
   
    """
    # We can now compile our pattern and use it to search text with re.compile()
    # Once we search the action we can check if theres a result, if the search returns "None" it does not match
    # So, we can return True if we get a result which means the action is valid
    re_pattern = re.compile(pattern)
    match = re_pattern.search(action)
 
    if(match != None):
        return [True, match.group(1)]
    else:
        return [False, ""]
 
def duel(action1:str, action2:str, action_set:dict):
    # Inorder to determine a winner we input the actions into the action_set dict
    # If the action is in the dict its a winning combo (order may change if order argument changed)
    # Once we know what wins against what we can return the winner
 
    if(action1 in action_set[action2]):
        return 2
    elif(action2 in action_set[action1]):
        return 1
    else:
        return 0 # Note: 0 represents a tie
 
class Player:
    def __init__(self, name:str):
        self.score = 0
        self.name = name
 
    def update_score(self, multiplier=1):
        # Add one times the multiplier to the players score
        self.score += (1 * multiplier)
 
    def get_score(self):
        # Return the score of the player
        return self.score
 
    # declares this as a shell of function that derived classes must implement
    # essentially allows us to use the same parameters & call this type of function despite the player type (cpu/human)
    @abstractmethod
    def action(self, action_set)->str: # declare return as string
        return "" # return a blank string
 
 
class HumanPlayer(Player): # inherits from player
    def __init__(self, name:str):
        super().__init__(name) # inherit __init__ from Player()
 
    def action(self, action_set):
        # To start the process of getting a user action we need to get input from the console
        # We can use the input function to achieve this
        user_action = str(input(f"{self.name}: "))
        check = validate(user_action, action_set)
 
        # By using the validate function previously created we can check if the input is a valid move
        # We enter the action into the functions arguments and check if it returns True
        # If it does not return True we ask the user to enter a new move,
        # once they enter a valid move we return it
 
        while(check[0] != True):
            print(":: Invalid input ::")
 
            user_action = str(input(f"{self.name}: "))
            check = validate(user_action, action_set)
 
        return str(check[1]).lower()
 
class CpuPlayer(Player): # inherits from Player
    def __init__(self, name:str):
        super().__init__(name) # inherit __init__ from Player()
 
    def action(self, action_set):
        # To choose an action the cpu needs the list of possible actions,
        # To get this we can use the keys function, which will return a list of possible moves
        possible_choices = list(action_set.keys())
 
        cpu_choice = choice(possible_choices) # now we get a random item from the list and return it as the move
        print(f"{self.name}: {cpu_choice}") # print the move so the user knows what happened
 
        return cpu_choice.lower()
      
