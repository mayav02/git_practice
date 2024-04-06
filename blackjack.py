import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))
        # ^ this was printed out!

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
    

print("Welcome to Blackjack!")    
player = input("You are starting with $500. Would you like to play a hand? ")
if player == 'yes':
    bet = int(input("Place your bet: "))
    if bet < 1:
        print("The minimum is $1. ")
    if bet >= 1:
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
        print("Would you like to hit or stay?")
                
        

else:
    print("Okay byeeeee!")
        
'''
class Card:
  def __init__(self, suit, rank):
    self.suit = suitåå
    self.rank = rank

class Deck:
  def __init__(self):
    self.cards = []
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
      for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
        self.cards.append(Card(suit, rank))

  def shuffle(self):
    random.shuffle(self.cards)
    ##print("dealer is: ", dealer)
    ##return dealer

  def draw(self):
    return self.cards.pop()
'''