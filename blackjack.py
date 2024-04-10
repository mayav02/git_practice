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
            for v in range(1,14):
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
                    bank =- bet
                    # Creating an instance of the class.
                    deck = Deck()
                    deck.shuffle()
                    player_hand = []
                    dealer_hand = []

                    for _ in range(2):
                        player_hand.append(deck.drawCard())
                        dealer_hand.append(deck.drawCard())

                    player_total = sum(card.blackjack_value() for card in player_hand)
                    print("You are dealt: ")
                    for card in player_hand:
                        card.show()
                    print("Total value of your hand:", player_total)
                    
                    dealer_total = sum(card.blackjack_value() for card in dealer_hand)
                    print("Dealer's cards:")
                    dealer_hand[0].show()
                    print("Unknown")
                    print("The dealer is dealt: " )
                    for _ in range(1):
                        deck.drawCard()
                        deck.show()
                    print("Total value of dealer's hand:", dealer_hand[0].blackjack_value())
                
                    first_hit_or_stay = input("Would you like to hit or stay? ")

                    if first_hit_or_stay == 'hit':
                            for _ in range(1):
                                print("You are dealt: ")
                                for _ in range(1):
                                    deck.drawCard()
                                    deck.show()
                                player_hand.append(deck.drawCard())
                                print("You now have ", player_hand)
                    # STOPPED RIGHT HERE!
                    if first_hit_or_stay == 'stay':
                        print("Your hand is now locked.")
                        for _ in range(2):
                            print("The dealer is dealt: " )
                            for _ in range(1):
                                deck.drawCard()
                                deck.show()
                        dealer_hand.append(deck.drawCard())    
                    if dealer_total <= 16:
                        deck.drawCard()
                        dealer_hand.append(deck.drawCard())
                        while dealer_total > 17:
                            print("Dealer will hit")
                            deck.drawCard()
                            dealer_hand.append(deck.drawCard())
            if player == 'no':
                print("Okay byeeeee!")

game = Play()
game.play_blackjack()
        