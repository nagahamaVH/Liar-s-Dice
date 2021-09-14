from numpy.random import randint
from icecream import ic

class Game():

   def __init__(self, players):
      """This method nitializes the game with a random player starting, and rolls the dice for all players."""
      self.players = players
      self.game_over = False
      self.bids = []
      self.n_dice = [5 for i in range(len(players))]
      self.current_player = players[randint(len(players))]
      self.roll_dice()

   def roll_dice(self):
      """The role dice method takes a list of integers representing the number of dice each player has
         and returns a list of lists where each list has the corresponding number of pseudo-random integers."""
         
      self.dice = [list(randint(low=1,high=7, size=i)) for i in self.n_dice]

   def eval_bid(self, bid):
      """This method returns the difference between the number of dice of the value bid on the table and the quantity bid."""
      (quantity, value) = bid
      actual_quantity = sum([sum([x == value or x == 6 for x in cup]) for cup in self.dice])
      return actual_quantity - quantity

   def eval_move(move):
      pass