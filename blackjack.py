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

    def play_black(self):
        while self.bank >= 500:
            print("Welcome to Blackjack!")    
            player = input(f"You are starting with ${bank}. Would you like to play a hand? ")
            if player == 'yes' and bank > 0:
                bet = int(input("Place your bet: "))
                if bet < self.min_bet:
                    print("The minimum is $1. ")
                if bet > self.mbank:
                    print("You don't have enough money for that bet.")
                else:
                    bank -= bet
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
                    print("Total value of dealer's hand:", dealer_hand[0].blackjack_value())

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
                                for _ in range(1):
                                    deck.drawCard()
                                deck.show()
                            for _ in range(2):
                                print("The dealer is dealt: " )
                                for _ in range(1):
                                    deck.drawCard()
                                    deck.show()
                    if first_hit_or_stay == 'stay':
                        print("locked")
                    deck.drawCard()
                    deck.show()

            if player == 'no':
                print("Okay byeeeee!")

Play()
        