import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

    def blackjack_value(self):
        if self.value in range(11,14):
            return 10
        else:
            return self.value
        

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,10):
                self.cards.append(Card(s,v))

    def show(self):
        dealers_choice = random.choice(self.cards)
        dealers_choice.show()
    
    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
    
class Play:
    def __init__(self):
        self.bank = 500
        self.min_bet = 1

    def play_blackjack(self):
        while self.bank >= 500:
            print("Welcome to Blackjack!")    
            player = input(f"You are starting with ${self.bank}. Would you like to play a hand? ")
            if player == 'yes' and self.bank > 0:
                bet = int(input("Place your bet: "))
                if bet < self.min_bet:
                    print("The minimum is $1. ")
                if bet > self.bank:
                    print("You don't have enough money for that bet.")
                else:
                    self.bank =- bet
                    deck = Deck()
                    deck.shuffle()
                    player_hand = []
                    dealer_hand = []

                    for _ in range(2):
                        player_hand.append(deck.drawCard())

                    dealer_hand.append(deck.drawCard())

                    player_total = sum(card.blackjack_value() for card in player_hand)
                    print("\nYou are dealt: ", end="")
                    for card in player_hand:
                        print("{} of {}  ".format(card.value, card.suit), end="")
                    print("\nTotal value of your hand:", player_total)
                    
                    dealer_total = sum(card.blackjack_value() for card in dealer_hand)
                    print("\nDealer's cards: ", end ="")
                    for card in dealer_hand:
                        print("{} of {}  ".format(card.value, card.suit), end="") 
                    # print("{} of {}  ".format(dealer_hand[0].value, dealer_hand[0].suit), end="")
                    # print("Unknown")
                    print("\nTotal value of dealer's hand:", dealer_total)
                    while player_total < 21:    
                        first_hit_or_stay = input("\nWould you like to hit or stay? ")
                        player_total = sum(card.blackjack_value() for card in player_hand)
                        if first_hit_or_stay == 'hit': 
                            if player_total < 21:
                                print("\nYou are dealt: ", end="")
                                card = deck.drawCard()
                                print("{} of {}  ".format(card.value, card.suit), end="")
                                player_hand.append(card)
                                player_total = sum(card.blackjack_value() for card in player_hand)
                                print("\nYou now have: ", end="")
                                for card in player_hand:
                                    print("{} of {}  ".format(card.value, card.suit), end="")
                                print("\nYour total is: ", player_total)
                                print(" ")
                                player_total = sum(card.blackjack_value() for card in player_hand)
                        if player_total >= 21:
                            print(f"BUST! You have gone over 21 and you lose {self.bank}. Play Again!")
                            exit
                        if first_hit_or_stay == 'stay':
                            print("Your hand is now locked.")
                            print("\nThe dealers face down card was: ", end="")
                            card = deck.drawCard()
                            dealer_hand.append(card)
                            dealer_total = sum(card.blackjack_value() for card in dealer_hand)
                            print("{} of {}  ".format(card.value, card.suit), end="")
                            print("\nAll of dealer's cards:", end="")
                            for card in dealer_hand:
                                print("{} of {}  ".format(card.value, card.suit), end="")
                                ##print("\nTotal value of dealer's hand:", dealer_total)
                            if dealer_total >= 17:
                                deck.drawCard()
                                card = deck.drawCard()
                                print(" ")
                                print("\nDealer will hit: {} of {}  ".format(card.value, card.suit))
                                dealer_hand.append(card)
                                dealer_total = sum(card.blackjack_value() for card in dealer_hand)
                                print("Dealer's total: ", dealer_total)
                            elif dealer_total > 17:
                                print("The dealer will hit: ", end="")
                                card = deck.drawCard()
                                print("{} of {}  ".format(card.value, card.suit), end="")
                                dealer_hand.append(card)
                                dealer_total = sum(card.blackjack_value() for card in dealer_hand)
                            if dealer_total >= 21:
                                print("You won! The dealer has gone over 21. Play again!")
            
            if player == 'no':
                print("Okay byeeeee!")

game = Play()
game.play_blackjack()