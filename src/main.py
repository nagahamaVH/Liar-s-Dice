from numpy.random import randint

def roll_dice(n_dice):
    """The role dice method takes a list of integers representing the number of dice each player has
       and returns a list of lists where each list has the corresponding number of pseudo-random integers."""
        
    return [list(randint(low=1,high=7, size=i)) for i in n_dice]
