from player import Player
import numpy as np
import random

class MCTS(Player):
    """"AI using MCTS algorithm"""
    def __init__(self, index, n_simulations):
        super().__init__(index)
        self.n_simulations = n_simulations

    def get_info(self, dices, bids, n_dices, player_order):
        self.dices = dices
        self.bids = bids
        self.n_dices = n_dices
        self.player_order = player_order

        # Generate info
        self.total_dices = sum(n_dices)
        # self.last_bid = self.get_last_bid()  # warning: redundant information

    def simulate_move(self):
        for _ in range(self.n_simulations):
            pass
            # self.search()
        # liar = "Liar"
        # spot_on_lose = "Spot on, lose two"
        # spot_on_gain = "Spot on, gain one"

    def search(self):
        has_ended = False
        oponent_action = ()

        # AI action
        action, has_ended = self.random_action()

        if has_ended:
            loss_i = self.loss_function(action, oponent_action)
        else:
            # Next player action
            oponent_action, _ = self.random_action()
            loss_i = self.loss_function(action, oponent_action)


    def random_action(self):
        action = random.randint(0, 3)
        if action == 0:
            return ("Liar", True)
        if action == 1:
            return ("Spot on, lose two", True)
        if action == 2:
            return ("Spot on, gain one", True)
        if action == 3:
            n_dice = random.randint(self.last_bid[0], self.total_dices)
            die_value = random.randint(1, 6)
            return ((n_dice, die_value), False)

    def loss_funtion(self, action, oponent_action):
        if action in ["Liar", "Spot on, lose two", "Spot on, gain one"]:
            pass
        else:
            pass

    # def get_last_bid(self):
    #     if self.bids == []:
    #         return []
    #     else:
    #         return self.bids[len(self.bids - 1)]

    def move(self, bids, player_dice, n_dice):
        print(self.dices)
        print(self.bids)
        print(self.n_dices)
        print(self.player_order)
        print("Current hand:", player_dice)
        turn_over = False
        command = input("Enter command: ")
        if command == "Liar" or command == "Spot on, lose two" or command == "Spot on, gain one":
            return command
        else:
            return tuple(map(int, command.split(' ')))