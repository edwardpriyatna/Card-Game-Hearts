from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from enum import Enum

#task 3
class Round:
    def __init__(self,players):
        self.players = players
        self.trick_number = 0
        self.trick = []
        self.broken_hearts = False
        self.one_round()

    def add_cards(self, begin_from=0, broken_hearts=False):
        'function to add cards to self.trick'
        'argument:'
        '-begin from: an integer, that is the index in players list where it starts from, for example is begin'
        'from 0 then begin from player 1'
        '-broken_hearts: a bool default to false, turns to true if card with suit hearts have been played'
        'returns self.trick'

        trick = self.trick
        players = self.players
        first_part = players[begin_from:]
        for player in first_part:
            played_card_first_part = player.play_card(trick, broken_hearts)
            print(player.__str__() + ' plays ' + played_card_first_part.__str__())
            if played_card_first_part.suit == Suit.Hearts and self.broken_hearts == False:
                self.broken_hearts = True
                print('Hearts have been broken!')
            trick.append(played_card_first_part)

        second_part = players[:begin_from]
        for player in second_part:
            played_card_second_part = player.play_card(trick, broken_hearts)
            print(player.__str__() + ' plays ' + played_card_second_part.__str__())
            if played_card_second_part.suit == Suit.Hearts and self.broken_hearts == False:
                self.broken_hearts = True
                print('Hearts have been broken!')
            trick.append(played_card_second_part)
            # print('trick is', trick)
        self.trick = trick
        # print('self trick after adding cards is',self.trick)
        return self.trick

    def find_winner(self, begin_from=0):
        'function to find winner of the trick'
        'arguments:'
        '-begin from: an integer, that is the index in players list where it starts from, for example is begin'
        'from 0 then begin from player 1'
        'returns the trick winner index'
        player_order_list = []
        player_number = begin_from
        for i in range(len(self.players)):  # make a list with the order the players go
            player_order_list.append(player_number)
            player_number += 1
            if player_number > len(self.players) - 1:
                player_number = 0
        current_suit = self.trick[0].suit
        cards_with_same_suit_as_current_suit = []
        for card in self.trick:
            if card.suit == current_suit:
                cards_with_same_suit_as_current_suit.append(card)
            else:
                continue
        max_card = max(cards_with_same_suit_as_current_suit)  # the max card of the current suit
        max_card_index = self.trick.index(max_card)
        trick_winner = player_order_list[max_card_index]
        takes_the_trick = 'player ' + str(trick_winner + 1) + ' takes the trick.'
        print(takes_the_trick, end='')
        return trick_winner

    def add_score_to_winner(self, winner_index=0):
        'function to add score to winner round score'
        'argument:'
        'winner_index: an integer which is the index of the player who won the trick'
        'returns point which is an integer of how many points the player gained'
        current_trick = self.trick[-len(self.players):]
        point = 0
        for card in current_trick:
            if card.suit == Suit.Hearts:  # counting how many cards with suit hearts
                point = point + 1
            elif card == Card(Rank.Queen, Suit.Spades):  # counting how many cards are queen of spades
                point = point + 13
        self.players[winner_index].round_score += point
        return point

    def end_of_round_stats(self):
        'function that displays end of round stats and determine shoot the moon'
        'has no argument and returns nothing'
        players = self.players
        shoot_the_moon_count = 0 #there is only one shoot the moon per round
        for player1 in self.players:
            if player1.round_score == 26 and shoot_the_moon_count == 0:
                shoot_the_moon_player = player1
                player1.round_score = player1.round_score - 26 #reduce shoot the moon player score
                shoot_the_moon_count += 1
                print(player1.__str__() + ' has shot the moon! Everyone else receives 26 points')
                for player2 in self.players:
                    if player2 != shoot_the_moon_player:
                        player2.round_score += 26 #add everyone else score

        for player in players:
            player.total_score += player.round_score #add player total score
            player.round_score = 0 #reset player round score
        return None

    def one_round(self):
        'a function that combines it all'
        'has no argument and returns nothing'
        trick = 0
        winner_index = 0
        if len(self.players) == 3:
            how_many_card_in_each_hand = 17
        elif len(self.players) == 4:
            how_many_card_in_each_hand = 13
        else:
            how_many_card_in_each_hand = 10
        while trick < how_many_card_in_each_hand:
            if len(self.trick) == 0:
                index = 0
                for player in self.players:
                    if Card(Rank.Two, Suit.Clubs) in player.hand:  # searching for player with two of clubs
                        winner_index = index
                    index += 1
            self.add_cards(winner_index, self.broken_hearts)
            winner_index = self.find_winner(winner_index)
            point = self.add_score_to_winner(winner_index)
            print(' Points received:', point)
            self.trick=[]
            trick = trick + 1
        self.end_of_round_stats()