from __future__ import annotations # for type hints of a class in itself

from enum import Enum
#task 1
class orderedRank(Enum):
    def __lt__(self, other):
        'function to compare if rank less than. argument is object card. returns a bool.'
        if self.value<other.value:
            return True
        else:
            return False

class Rank(orderedRank):
    'a class containing rank and their values'
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

class orderedSuit(Enum):
    def __lt__(self, other):
        'function to compare if suit less than. argument is object card. returns a bool.'
        if self.value<other.value:
            return True
        else:
            return False

class Suit(orderedSuit):
    'class containing suits and their values'
    Clubs = 1
    Diamonds = 2
    Spades = 3
    Hearts = 4

class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def __eq__(self, other):
        'function to know if cards are equal. argument is object card. returns a bool.'
        if self.rank==other.rank and self.suit==other.suit:
            return True
        else:
            return False

    def __lt__(self, other):
        'function to know if cards are less than. argument is object card. returns a bool.'
        if self.suit==other.suit:
            if self.rank < other.rank:
                return True
            else:
                return False

    def __str__(self):
        return str(self.rank.name) + ' of ' + str(self.suit.name)

    def __repr__(self):
        return self.__str__()