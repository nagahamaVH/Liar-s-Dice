from player import Player

class Human(Player):
    """"The Human class provides an interface through which humans may play the game."""

    def move(self, bids, player_dice, n_dice):
        print("Current hand:", player_dice)
        turn_over = False
        command = input("Enter command: ")
        if command == "Liar" or command == "Spot on, lose two" or command == "Spot on, gain one":
            return command
        else:
            return tuple(map(int, command.split(' ')))
