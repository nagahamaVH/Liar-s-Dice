from abc import ABCMeta, abstractmethod
from tokenize import String
from typing import Tuple, final, Union

class Player(metaclass = ABCMeta):
    """The Player class is an abstract base class from which all
       game playing AIs must inherit."""
    
    @final
    def __init__(self, index) -> None:
        self.index = index

    @abstractmethod
    def move(self, bids, dice) -> Union[str, Tuple[int, int]]:
        """Make a move based on dice value and bids in round."""