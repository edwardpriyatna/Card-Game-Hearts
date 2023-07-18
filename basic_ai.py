from __future__ import annotations
from cards import Card, Rank, Suit
from enum import Enum
#task 2
class BasicAIPlayer:
    def __init__(self,name,hand=[]):
        self.name=name
        self.hand=hand
        self.round_score=0
        self.total_score=0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def check_valid_play(self, card, trick, broken_hearts=False):
        """
          This function checks if the card can be played
          Arguments:
            - card: a card object
            - trick: a list of cards in current trick
            - broken_hearts: a bool, becomes true if card with suit hearts have been played
          Returns a tuple with the first being a bool, the second being a message
        """
        if len(trick) == 0:  # for example if list has len of 4, that means the next play is a lead trick
            lead_trick = True  # checking if lead_trick is true
        else:
            lead_trick = False

        if len(trick) == 0:
            leading_suit = 0
        else:
            leading_suit = trick[0].suit

        if lead_trick == True:
            if Card(Rank.Two, Suit.Clubs) in self.hand:
                if card == Card(Rank.Two, Suit.Clubs):  # if playing card with rank two and suit clubs it returns True
                    return (True, 'valid play')
                else:
                    # print("you need to play Two of Clubs")
                    return (False, "you need to play Two of Clubs")
            elif broken_hearts == False:
                if card.suit == Suit.Hearts:  # if the player tries to play hearts, it checks if there are other options
                    heart_count = 0
                    for card in self.hand:  # searching if there are any other card than hearts
                        if card.suit == Suit.Hearts:
                            heart_count = heart_count + 1
                    if heart_count == len(self.hand):  # if there are no other card than hearts
                        # print(card,'no other than hearts, you can lead trick with hearts')
                        return (True, 'valid play')  # the player can play card with the suit hearts
                    else:  # if there are other card than hearts, the player can't play  hearts
                        # print(card,"for leading a trick, if there are other card than hearts. The player can't play  hearts")
                        return (False,"for leading a trick, if there are other card than hearts. The player can't play  hearts")
                else:
                    # print(card,'you can lead with any card except card with suit.hearts')
                    return (True, 'you can lead with any card except card with suit.hearts')
            else:
                # print('you can lead with any card you want')
                return (True, 'valid play')
        else:
            if Card(Rank.Two, Suit.Clubs) in trick:  # check if it is first trick of the round
                if card.suit == leading_suit:
                    return (True, 'card has the same suit')
                else:
                    queen_spades_count = 0
                    heart_count = 0
                    for card in self.hand:
                        if card.suit == leading_suit:
                            return (False, "Player still has cards from the suit of the current trick for len(trick)<5")
                        elif card == Card(Rank.Queen, Suit.Spades):
                            queen_spades_count = queen_spades_count + 1
                        elif card.suit == Suit.Hearts:
                            heart_count = heart_count + 1
                        else:
                            continue
                    if queen_spades_count + heart_count == len(self.hand):
                        return (True, 'you can play heart or queen of spades since you only have those cards')
                    else:
                        return (True, 'since you dont have cards from the current suit, you can play any suit')

            elif card.suit == leading_suit:  # if card.suit equals the leading card suit
                return (True, 'the current card.suit equals the last card suit')
            else:
                for card in self.hand:
                    if card.suit == leading_suit:
                        return (False, "Player still has cards from the suit of the current trick")
                return (True, 'since you dont have cards from the current suit, you can play any suit')

    def play_card(self,trick,broken_hearts):
        """
        This function plays the three lowest card that are valid
        Arguments:
        - trick: a list of cards in current trick
        - broken_hearts: a bool, becomes true if card with suit hearts have been played
        Returns played card which is a card object
        """
        valid_cards=[]
        for card in self.hand:
            if self.check_valid_play(card,trick,broken_hearts)[0]==True:
                valid_cards.append(card)
        played_card=min(valid_cards)
        self.hand.remove(played_card)
        return played_card

    def pass_cards(self):
        """
        This function passes the three highest card in hand
        Arguments: none
        Returns a list containing three card objects
         """
        passed_cards=[]
        for i in range (3):
            current_max=max(self.hand)
            passed_cards.append(current_max)
            self.hand.remove(current_max)
        return passed_cards


if __name__ == "__main__":
    # Test your function here
    #player = BasicAIPlayer("Test Player 1")
    #player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
    #trick, broken_hearts = [Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades)], False
    #print(player.check_valid_play(player.hand[0], trick, broken_hearts))
    pass
