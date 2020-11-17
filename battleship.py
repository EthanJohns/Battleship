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
        self.ships = ["cruiser","battleship","destroyer","submarine","patrol"]
        self.valid_commands = ["place", "start", "quit"]

        self.examaple_player_grid =[[" ","1","2","3","4","5","6","7","8","9","10"],
                                    ["A"," "," "," "," "," "," "," "," "," "," "],
                                    ["B"," ","C","C","C","C","C"," "," "," "," "],
                                    ["C"," "," "," "," "," "," "," "," "," "," "],
                                    ["D"," "," "," "," "," "," "," "," "," "," "],
                                    ["E"," "," "," "," "," "," "," ","P","P"," "],
                                    ["F"," ","S"," "," ","B"," "," "," "," "," "],
                                    ["G"," ","S"," "," ","B"," "," "," "," "," "],
                                    ["H"," "," "," "," ","B"," "," ","D","D","D"],
                                    ["I"," "," "," "," ","B"," "," "," "," "," "],
                                    ["J"," "," "," "," "," "," "," "," "," "," "]]

def help(game, message):
    if message == "start":
        print ("""Welcome to Battleship.\n""")

    if message in ["start", "help"]:
        print(f"""You have the following ships:
    Cruiser:      #####    Size: 5
    Battleship:   ####     Size: 4
    Destroyer:    ###      Size: 3
    Submarine:    ###      Size: 3
    Patrol:       ##       Size: 2

The following commands are available:
    place "ship" "range" - Places a ship in a valid range: (place cruisier B2-B6)
    start - Starts game after ships have been placed
    quit - Quits the program\n""")


def print_grid(game):

    for row in game.player_grid:
        for square in row:
            print (square, end = '|')
        print("")

def place_ship(game, command_list):
    # TODO
    pass

def validate_placement(game, command_list):
    # TODO
    pass

def validate_range(game, command_list):
    range_list = command_list[2].split('-')

    if len(range_list) != 2:
        return False, f"""Error: "{command_list[2]}" is not a valid range."""

    elif not (range_list[0][1].isdigit() or range_list[0][1].isdigit()):
        return False, f"""Error: "{command_list[2]}" is not a valid range."""

    elif not ('A' <= range_list[0][0] <= 'J' and 1 <= int(range_list[0][1]) <= 10):
        return False, f"""Error: "{command_list[2]}" is not a valid range."""

    elif not ('A' <= range_list[1][0] <= 'J' and 1 <= int(range_list[1][1]) <= 10):
        return False, f"""Error: "{command_list[2]}" is not a valid range."""

    else:
        return validate_placement(game, command_list)

def validate_command(game, command_list):

    if not command_list[0].lower() in ["place", "start", "quit"]:
        return False, f"""Error: Command "{command_list[0]}" not understood."""

    elif not len(command_list) == 3 and command_list[0].lower() == "place":
        return False, f"""Error: Incorrect number of commands."""

    elif len(command_list) == 3 and not command_list[1].lower() in game.ships:
        return False, f"""Error: "{command_list[1]}" is not a valid ship."""

    elif len(command_list) == 3 and command_list[1].lower() in game.ships:
        return validate_range(game, command_list)
    else:
        return True, "No Error"

def process_commands(game):

    command = input("\nInput Command: ")
    command_list = command.split()
    valid, error_ouput = validate_command(game, command_list)


    if not valid:
        print(error_ouput)
    elif command_list[0].lower() == "quit":
        exit()
    elif command_list[0].lower() == "place":
        place_ship(game, command_list)

    return True

    # if command[0].lower() == "":
    #     run_login()
    # elif command.lower() == "logout":
    #     run_logout()
    # elif not user_name or not user_email:
    #     raise Exception("Please Login")
    # elif command.lower() == "help":
    #     run_help()
    # elif command.lower() == "calendar":
    #     run_calendar()
    # elif command.lower() == "host":
    #     run_host(user_email, user_name)
    # elif command.lower() == "attend":
    #     run_attend(user_email, user_name)
    # elif command.lower() == "delete":
    #     run_delete(user_email, user_name)
    # else:
    #     raise Exception(f""""{command}" is not a valid command""")

def run_game():
    """Runs the game from beginning."""
    
    
    game = Battleship()
    help(game, "start")
    print_grid(game)

    while True:
        if not process_commands(game):
            break



run_game()