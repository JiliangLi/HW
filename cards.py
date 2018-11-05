class Card:
	def __init__ (self, suit, rank=0):
		self.suit = suit
		self.rank = rank
	
	def __str__(self):
		return str(self.rank) + " of " + self.suit

class Deck:
	def __init__ (self):
		suit = ["club", "spade", "heart", "diamond", "Joker"]
		rank = [i for i in range(1, 14)]
		self.cards = []
		for i in rank:
			for j in suit:
				self.cards.append(Card(j, i))
		self.cards.append(Card(suit[4]))

	def __str__ (self):
		return str(self.cards)

myDeck = Deck()
print(Deck())