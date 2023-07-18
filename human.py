from __future__ import annotations
from enum import Enum
from cards import Card,Rank,Suit
from player import Player


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self, name='empty')
        self.name = self.enter_name()

    def enter_name(self):
        'prompts the user to input a name'
        'has no arguments and return self.name'
        self.name = input('Please enter your name:')
        return self.name

    def get_hand(self):
        return self.hand

    def input_play_card_index(self):  # prompts the user for an input to play their cards
        'checks for a valid integer input when playing a card'
        'has no arguments'
        'input needs to be an integer between o to len(self.hand)-1, if not it will loop and ask for input again'
        'if correct input returns the played card index'
        while True:
            print('your hand is',self.hand)
            try:
                human_card_index = int(input('input your number(0-' + str(len(self.hand) - 1) + '):'))
                if human_card_index < 0 or human_card_index > len(self.hand) - 1:
                    print('wrong index')
                    continue
                return human_card_index
            except ValueError:
                print('wrong input')  # if invalid index number inputted
                continue

    def play_card(self, trick, broken_hearts):
        while True:
            human_card_index = self.input_play_card_index()
            human_played_card = self.hand[human_card_index]
            print(self.name, 'plays', human_played_card)
            if self.check_valid_play(human_played_card, trick, broken_hearts)[0] == True:  # checks to see if card played is valid
                # print('valid play')
                self.hand.remove(human_played_card)  # removes card played from hand
                return human_played_card
            else:
                print(self.check_valid_play(human_played_card, trick, broken_hearts))
                print('invalid play')
                continue

    def input_pass_cards_index(self):
        'checks for a valid integer input when passing cards'
        'has no arguments'
        'input needs to be 3 comma separated integers and needs to be valid index, if not it will loop and ask for input again'
        'if correct input returns the played card index'
        while True:
            print('your hand is', self.hand)
            human_index_input = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
            human_index_input_list = human_index_input.split(',')
            try:
                numbers = [int(x.strip()) for x in human_index_input_list]  # splits the input into 3 numbers with the use of commas
                if len(numbers) == 3:
                    valid_number_count = 0
                    for number in numbers:
                        if number > -1 and number < len(self.hand):  # valid inputs accepted
                            valid_number_count += 1
                            if valid_number_count == 3:
                                return numbers
                    print('number need to be between 0 to', len(self.hand) - 1)
                    continue
                else:
                    print('you need 3 numbers')
                    continue
            except:
                print('please try again, with only numbers separated by commas (e.g. "1, 5, 3")')
                continue

    def pass_cards(self, pass_to):  # function to pass the inputted cards to other players
        'function to pass the inputted cards to other players'
        'argument pass_to is an integer. It mean player pass to which player'
        'returns passed cards list which is a list containing passed card objects'
        pass_cards_index_list = self.input_pass_cards_index()
        pass_cards_index_list.sort()  # sorts the passed cards index by ascending order
        passed_cards_list = []
        for pass_index1 in pass_cards_index_list:
            passed_card = self.hand[pass_index1]  # index out of range because card before removed
            passed_cards_list.append(passed_card)
        print(self.name + ' passed ' + str(passed_cards_list) + ' to player ' + str(pass_to))
        pass_cards_index_list.reverse()
        for pass_index2 in pass_cards_index_list:  # removing the cards
            removed_card = self.hand[pass_index2]
            self.hand.remove(removed_card)
        return passed_cards_list


if __name__ == "__main__":
    human_player1 = HumanPlayer()
    human_player1.hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades),Card(Rank.Six, Suit.Diamonds),
                          Card(Rank.Three,Suit.Diamonds),Card(Rank.King,Suit.Hearts),Card(Rank.Queen,Suit.Spades),Card(Rank.Jack,Suit.Clubs)]
    trick = [Card(Rank.Two,Suit.Clubs)]
    human_player1.pass_cards(2)
    human_player1.play_card(trick,False)