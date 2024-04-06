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