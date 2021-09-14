from abc import ABCMeta, abstractmethod

class Player(metaclass = ABCMeta):
    """The Player class is an abstract base class from which all
       game playing AIs must inherit."""
    
    @abstractmethod
    def move(self, bids, dice):
        """Make a move based on dice value and bids in round."""