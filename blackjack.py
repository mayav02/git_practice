import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

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
    
bank = 500
min_bet = 1

while bank >= 500:
    print("Welcome to Blackjack!")    
    player = input(f"You are starting with ${bank}. Would you like to play a hand? ")
    if player == 'yes' and bank > 0:
        bet = int(input("Place your bet: "))
        if bet < min_bet:
            print("The minimum is $1. ")
        if bet >= min_bet:
            bank =- bet
            deck = Deck()
            deck.build()
            deck.shuffle()
            for _ in range(1):
                print("You are dealt: ")
                for _ in range(2):
                    deck.drawCard()
                    deck.show()
            for _ in range(1):
                print("The dealer is dealt: " )
                for _ in range(1):
                    deck.drawCard()
                    deck.show()
                    print("Unknown")
            first_hit_or_stay = input("Would you like to hit or stay?")
            if first_hit_or_stay == 'hit':
                    for _ in range(1):
                        print("You are dealt: ")
                        for _ in range(2):
                            deck.drawCard()
                            deck.show()
            if first_hit_or_stay == 'stay':
                for _ in range(1):
                    print("The dealer is dealt: " )
                    for _ in range(1):
                        for _ in range(2):
                            deck.drawCard()
                            deck.show()
                
    if player == 'no':
        print("Okay byeeeee!")
        