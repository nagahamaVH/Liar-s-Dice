# Liar's Dice

The purpose of this repository is to provide an interface for the game Liar's Dice, which may be used to train and evaluate various game playing agents.

## Rules of the Game
Liar’s dice is a game for two or more players. The object of the game is to be the last player with dice. Each player begins with 5 dice and a cup. At the beginning of each round all players shake their dice in their cup and then turn the cup over, being sure to conceal the values of their dice. For the first round a randomly selcted player begins by making a bid. A bid is a statement about
the number of dice of a certain value there are collectively i.e. including all
opponents dice. The following player then has three options:

1. They may make a higher bid i.e. they claim that there are a higher number of dice of a certain value (which is not necessarily the same value as the previous players bid).

2. They may call the preceding player a liar. In this case all players reveal their dice and should there be less than the number of dice the preceding player bid then that player loses a die. However, Should there be the same number bid, or more, then the player who challenged the bid loses a die.

3. The player could alternatively say “Spot on”. In this case as well all players reveal their dice. However, if the preceding players bid happens to be exactly the case then the challenging player can either: reclaim a lost die, or force the previous player to lose two dice. Should the bid happen to be false i.e. there were more or less dice of a certain value bid then the challenging player loses a die.

Once a challenge is made the round ends and a new round begins, and the player to the left of the loser of the challenge begins the next round. This continues until only one player has dice remaining.

Finally, there are a couple of extra rules involving sixes. A die with a value of six is *wild* and can take on any value. For instance if a player made a bid that there were five dice with value of three on the table, and the following player challenged, then if there were four threes and three sixes, then we would say there are seven threes on the table. Consequently, to account for how much less likely there are to be a certain number of sixes on the table than the same number of another value, sixes are worth double for the purposes of bidding. For example if a player bid three fives, then the following player could bid two sixes as the value of two sixes is four. Alternatively if a player bid two sixes then the following player would need to bid at least five of another value, or three sixes.

## Game Playing Agent Specifications
Any game playing agent you wish to implement must inheret from the abstract base class `Player`, and implement the method `move`. The method `move` must take the following arguments:

- `bids` : a list of tuples representing all of the bids made by players in the current round. Each tuple consists of a pair of Integers; the first defining the quantity bid, and the second the value bid. i.e. three fives is represented by (3, 5).

- `player_dice` : a list of integers which represents the dice the player has rolled for the current round.

- `n_dice` : a list representing the quantity of dice each player in the game has.

The `move` method must return either a tuple representing a valid bid (in the format described above), or a string representing a challenge which must be one of:

- "Liar"

- "Spot on, lose two"

- "Spot on, gain one"

Lastly, the agent has the property `index` which represents their order in the game play i.e. a player with an index of 3 plays after a player of index 2, and before a player of index 3. A random index is chosen to determine which player starts in the first round. The same indexing is used for the `n_dice` variable, so agents may query the number of dice belonging to all other players.