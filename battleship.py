import random

class Battleship:
    def __init__(self):
        self.ai_name = ""
        self.player_grid = [[" ","1","2","3","4","5","6","7","8","9","10"],
        ["A"," "," "," "," "," "," "," "," "," "," "],
        ["B"," "," "," "," "," "," "," "," "," "," "],
        ["C"," "," "," "," "," "," "," "," "," "," "],
        ["D"," "," "," "," "," "," "," "," "," "," "],
        ["E"," "," "," "," "," "," "," "," "," "," "],
        ["F"," "," "," "," "," "," "," "," "," "," "],
        ["G"," "," "," "," "," "," "," "," "," "," "],
        ["H"," "," "," "," "," "," "," "," "," "," "],
        ["I"," "," "," "," "," "," "," "," "," "," "],
        ["J"," "," "," "," "," "," "," "," "," "," "]]
        self.ships = ["Cruiser","Battleship","Destroyer","Submarine","Patrol Boat"]

def help(game, message):
    if message == "start":
        print ("""Welcome to Battleship.\n""")

    if message in ["start", "help"]:
        print(f"""You have the following ships:
    Cruiser:      #####    Size: 5
    Battleship:   ####     Size: 4
    Destroyer:    ###      Size: 3
    Submarine:    ###      Size: 3
    Patrol Boat:  ##       Size: 2\n""")


def print_grid(game):

    for row in game.player_grid:
        for square in row:
            print (square, end = '|')
        print("")


def run_game():
    """Runs the game from beginning."""
    
    
    game = Battleship()
    help(game, "start")
    
    print_grid(game)



run_game()