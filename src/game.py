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
        print("Player %d is starting.".format(self.current_player.index))
        self.previous_player = None
        self.roll_dice()

    def play_game(self, players):
        self.new_game(players)

    def roll_dice(self):
        """The role dice method takes a list of integers representing the number of dice each player has
            and returns a list of lists where each list has the corresponding number of pseudo-random integers."""
            
        self.dice = [list(randint(low=1,high=7, size=i)) for i in self.n_dice]

    def get_actual(self, value):
        """This method finds the actual number of dice of a given value on the table."""
        actual = sum([sum([x == value or x == 6 for x in cup]) for cup in self.dice])
        print("There are %d %ds on the table.".format(actual, value))
        return actual

    def eval_bid(self, bid):
        """This method returns the difference between the number of dice of the value bid on the table and the quantity bid."""
        (quantity, value) = bid
        return self.get_actual(value) - quantity

    def is_valid_challenge(self, move):
        """This method checks is a move is a valid challenge."""
        return (type(move) == str) and any(self.bids) and (move == "Liar" or move == "Spot on lose two" or (move == "Spot on gain 1" and self.n_dice[self.current_player.index] <= 5))

    def is_valid_bid(self, move):
        """This method checks if a move is a valid bid."""
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
            print("Invalid move. Player %d disqualified.".format(self.current_player.index))
            self.n_dice[self.current_player.index] = 0
        

    def execute_challenge(self, challenge):
        """This method evaluates the consequences of a player challenging."""
        value = self.eval_bid(self.bids[-1])
        if challenge == "Liar":
            if value >= 0:
                self.n_dice[self.current_player.index] -= 1
                self.current_player = self.get_next_player()
            else:
                self.n_dice[self.previous_player.index] -=1
        elif challenge == "Spot on lose two":
            print("Player %d calls 'Spot on'.")
            if value == 0:
                self.n_dice[self.previous_player.index] -= 2
            else:
                self.n_dice[self.current_player.index] -= 1
                self.current_player = self.get_next_player()
        else:
            if value == 0:
                self.n_dice[self.current_player.index] += 1
            else:
                self.n_dice[self.current_player.index] -= 1
                self.current_player = self.get_next_player()

    def execute_bid(self, bid):
        """This method appends the playes bid to the bids structure and moves to the next player."""
        self.bids.append(bid)
        print("Player %d bids %d %ds.".format(self.current_player.index, *bid))
        self.previous_player = self.current_player
        self.current_player = self.get_next_player()
        
    def get_next_player(self):
        """This method returns the next player with remaining dice."""
        current_index = self.current_player.index
        while True:
            if self.n_dice[(current_index + 1) % len(self.players)] > 0:
                return self.players[current_index + 1]
            else:
                current_index += 1