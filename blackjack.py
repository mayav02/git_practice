import random
from card import Card

class Deck:
    def __init__(self):
        pass

    def create_deck(self):
        pass

    def shuffle(self):
        pass

    def deal(self, num_cards):
        pass

class Card:
    SUIT_SYMBOLS = {
        0: u"\u2666",  # diamonds
        1: u"\u2665",  # hearts
        2: u"\u2663",  # clubs
        3: u"\u2660"  # spades
    }

    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        pass

    def __str__(self):
        pass

class Dealer:
    def __init__(self):
        pass

    def get_str_hand(self):
        pass

    def hit(self):
        pass

from deck import Deck
from hand import Hand

class Game:

    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

        print("Welcome to Blackjack!")
        player = input("You are starting with $500. Would you like to play a hand? ")
        while player == 'yes':
            bet = int(input("Place your bet: "))
            if bet < 1:
                print("The minimum is $1. ")
            else:
                break
        return bet

    def start_game(self):
        random.shuffle(Deck)
        pass

class Hand:
    def __init__(self):
        pass

    def get_value(self):
        pass
        
    def add_to_hand(self):
        pass

    def __str__(self):
        pass

class Player:
    def __init__(self, balance):
        self.balance = balance

    def get_str_hand(self):
        pass


Game(Player, Dealer)