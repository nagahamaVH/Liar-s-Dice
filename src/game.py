import re
from numpy.random import randint
from icecream import ic

class Game():

    def new_game(self, players):
        """This method nitializes the game with a random player starting, and rolls the dice for all players."""
        self.players = players
        self.game_over = False
        self.bids = []
        self.n_dice = [5 for i in range(len(players))]
        self.current_player = players[randint(len(players))]
        self.roll_dice()

    def play_game(self, players):
        self.new_game(players)

    def roll_dice(self):
        """The role dice method takes a list of integers representing the number of dice each player has
            and returns a list of lists where each list has the corresponding number of pseudo-random integers."""
            
        self.dice = [list(randint(low=1,high=7, size=i)) for i in self.n_dice]

    def eval_bid(self, bid):
        """This method returns the difference between the number of dice of the value bid on the table and the quantity bid."""
        (quantity, value) = bid
        actual_quantity = sum([sum([x == value or x == 6 for x in cup]) for cup in self.dice])
        return actual_quantity - quantity

    def is_valid_challenge(self, move):
        """This method checks is a move is a valid challenge."""
        return (type(move) == str) and any(self.bids) and (move == "Liar" or move == "Spot on")

    def is_valid_bid(self, move):
        if type(move) == tuple:
            if any(self.bids):
                if move[0] > self.bids[-1][0] and (move[1] >= 1 and move[1] <= 6):
                    return True
                else:
                    return False
            elif move[0] >= 1 and (move[1] >= 1 and move[1] <= 6):
                return True
        else:
            return False

    def execute_move(self, move):
        """Executes the move submitted by the player."""
        if self.is_valid_bid(move):
            self.execute_bid(move)
        elif self.is_valid_challenge(move):
            loser = self.execute_challenge(move)
            print("New round. Player %d starting".format((loser + 1) % len(self.players)))
        else:
            print("Invalid move. Player disqualified.")
            self.n_dice[self.current_player.index] = 0
        

    def execute_challenge(self, challenge):
        pass

    def execute_bid(self, bid):
        pass