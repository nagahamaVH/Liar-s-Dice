from player import Player

class Skeptic(Player):
    """The skeptic class implements a player who always believes the 
       preceding player is lying."""

    def move(self, bids, dice):
        """The move method returns ('Liar') if bids is not empty and (1,1) otherwise."""
        if any(bids):
            return 'Liar'
        else:
            return (1,1)