from __future__ import annotations
import random
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from round import Round
from enum import Enum

class Hearts:

    def __init__(self):
        self.players=[]
        self.target_score = 0
        self.number_of_players = 0
        self.round_number = 1
        self.one_heart()

    def enter_target_score(self):
        'function to enter target score that checks for invalid input'
        'target score is a positive integer'
        while True:
            try:
                self.target_score = int(input("Please enter a target score to end the game: "))
                if self.target_score<0:
                    continue
                return self.target_score
            except ValueError:
                continue

    def enter_number_of_players(self):
        'function to enter number of players that checks for invalid input'
        'number of players is an integer from 3 to 5'
        while True:
            try:
                self.number_of_players = int(input("Please enter the number of players (3-5): "))
                #print('======== Starting round '+ str(self.round_number) + ' ========')
                if self.number_of_players<3 or self.number_of_players>5:
                    continue
                return self.number_of_players
            except ValueError:
                continue

    def generate_a_deck(self):
        'this function generates a deck of card'
        'has no argument and return a deck which is a list containing card objects'
        number_of_players = self.number_of_players
        deck = []
        rank_list = [Rank.Two, Rank.Three, Rank.Four, Rank.Five, Rank.Six, Rank.Seven, Rank.Eight,
                     Rank.Nine, Rank.Ten, Rank.Jack, Rank.Queen, Rank.King, Rank.Ace]
        suit_list = [Suit.Clubs, Suit.Diamonds, Suit.Spades, Suit.Hearts]
        for suits in suit_list:
            for ranks in rank_list:
                deck.append(Card(ranks, suits))

        if number_of_players == 3:
            deck.remove(Card(Rank.Two, Suit.Diamonds))
        elif number_of_players == 5:
            deck.remove(Card(Rank.Two, Suit.Diamonds))
            deck.remove(Card(Rank.Two, Suit.Spades))
        return deck

    def generate_players(self):
        'this function generates players which is a list of basicAIplayers'
        'has no arguments and return self.players'
        number_of_players=self.number_of_players
        for i in range(number_of_players):
            new_player=BasicAIPlayer('Player '+str(i+1) )
            self.players.append(new_player)
        return self.players

    def shuffle_cards(self):
        'function to shuffle cards'
        'this function updates the player hand'
        'has no arguments and returns nothing'
        deck = self.generate_a_deck() #creating a deck of cards
        if self.number_of_players==3:
            card_number_for_each_player=17
        elif self.number_of_players==5:
            card_number_for_each_player=10
        else:
            card_number_for_each_player=13

        for player in self.players: #adding random cards to players
            player.hand=[]
            for added_cards in range(card_number_for_each_player):
                random_index = random.randint(0, len(deck)-1)
                random_card = deck[random_index]
                player.hand.append(random_card)
                deck.pop(random_index)
            print(player.__str__()+ " was dealt " +str(player.hand) )

    def passing_cards(self):
        'function to pass cards'
        'this function updates the player hand'
        'has no arguments and returns nothing'
        if self.round_number > self.number_of_players:
            pass_to = self.round_number % self.number_of_players # pass to is used to determine pass to how many player after that player
        elif self.number_of_players == 3:
            if self.round_number == 1:
                pass_to = 1
            elif self.round_number == 2:
                pass_to = 2
            else:
                pass_to = 0
        elif self.number_of_players == 4:
            if self.round_number == 1:
                pass_to = 1
            elif self.round_number == 2:
                pass_to = 2
            elif self.round_number == 3:
                pass_to = 3
            else:
                pass_to = 0
        else:
            if self.round_number == 1:
                pass_to = 1
            elif self.round_number == 2:
                pass_to = 2
            elif self.round_number == 3:
                pass_to = 3
            elif self.round_number == 4:
                pass_to = 4
            else:
                pass_to = 0

        passed_cards_nested_list=[] #a nested list containing a list of passed cards
        for player in self.players:
            passed_cards1=player.pass_cards()
            passed_cards_nested_list.append(passed_cards1)

        for passed_cards2 in passed_cards_nested_list: #appending the passed cards in passed card nested list to players
            passed_card_list_index=passed_cards_nested_list.index(passed_cards2)
            append_to=passed_card_list_index+pass_to
            if append_to>len(self.players)-1: #pass wrap around
                append_to= append_to - len(self.players)
            print('Player '+str(passed_card_list_index+1)+' passed '+str(passed_cards2)+' to Player '+str(append_to+1))
            for card in passed_cards2:
                self.players[append_to].hand.append(card)

    def one_heart(self):
        'function that combines it all'
        'returns true if the game ends'
        self.enter_target_score()
        self.enter_number_of_players()
        players = self.generate_players()
        while True:
            print('======== Starting round ' + str(self.round_number) + ' ========')
            self.shuffle_cards()
            self.passing_cards()
            Round(players)
            print('======== End of round ' + str(self.round_number) + ' ========')
            for player in self.players: #print end of round stats
                print(player.__str__().capitalize() + '\'s ' + "total score: " + str(player.total_score))
            if self.check_end_game() == True:
                return True
            self.round_number = self.round_number + 1

    def check_end_game(self):
        'function to check if game ends'
        'has no argument and returns bool'
        for player in self.players:
            if player.total_score>=self.target_score: #check if a player has reached the target score
                if self.find_winner()==True:
                    return True
                else:
                    return False
        return False

    def find_winner(self):
        'function to determine if there is a winner or if a tie happens'
        'has no arguments and returns bool'
        players_final_score=[]
        for player in self.players:
            players_final_score.append(player.total_score)
        hearts_winner_score=min(players_final_score)
        for player2 in self.players:
            if player2.total_score==hearts_winner_score:
                heart_winner_player=player2
        for player3 in self.players:#check if there is a tie
            if player3.total_score==hearts_winner_score and player3!=heart_winner_player:
                return False
        hearts_winner_index=players_final_score.index(hearts_winner_score)
        print('Player '+str(hearts_winner_index+1)+' is the winner!')
        return True

if __name__ == "__main__":
	Hearts()