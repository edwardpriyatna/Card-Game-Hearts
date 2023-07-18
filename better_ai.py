from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player
from basic_ai import BasicAIPlayer

class BetterAIPlayer(Player):
        def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
                'function to play cards'
                'arguments:'
                '-trick is a list of card objects'
                '-broken hearts is a bool'
                'return card_played which is an object card'
                valid_cards = []
                valid_cards.sort() #valid cards are sorted in ascending order
                card_played = ""
                for card in self.hand:
                        if Player.check_valid_play(self,card,trick,broken_hearts)[0]==True: #checks to see if card played is valid
                                valid_cards.append(card)
                card_played  = valid_cards[0] # card played is the lowest card available
                self.hand.remove(card_played) # card played is removed from player's hand
                return card_played


        def pass_cards(self) -> list[Card]:
                'function to pass the inputted cards to other players'
                'has no arguments'
                'returns passed cards list which is a list containing passed card objects'
                passed_cards_list=[]
                while len(passed_cards_list) < 3: #when AI has not passed 3 cards yet
                        rank_to_pass = 2 #initialized as the lowest value in cards
                        for card in self.hand:
                                if card == Card(Rank.Two, Suit.Clubs): #this is so the AI does not start the game, hence giving it an advantage
                                        passed_cards_list.append(card)
                                        self.hand.remove(card)
                                if card.rank.value >= rank_to_pass: #checks if a card is greater or equal to value 2
                                        rank_to_pass = card.rank.value
                                        card_passed = card

                        passed_cards_list.append(card_passed) #adds the card passed to the passed cards list
                        self.hand.remove(card_passed) #card passed is removed from player's hand

                return passed_cards_list