class Card:

    def __init__(self, theName, theType, theHP, theMoves, isShiny):
        self.name = theName
        self.type = theType
        self.HP = theHP
        self.moves = theMoves
        self.Shiny = isShiny

    def __str__(self):
        return 'name: {self.name}, type: {self.type}, HP: {self.HP}, moves: {self.moves}, isShiny: {self.Shiny}.'.format(self=self)


class Deck:

    deckCards = 0

    @classmethod
    def openCard(cls):
        Deck.deckCards += 1
        print('Cards in the deck are {cls.deckCards}'.format(cls=cls))

    def __init__(self):
        self.card = []

    def addCard(self, theCard):
        self.card.append(theCard)

    def viewCards(self):
        for c in self.card:
            print(c)


c1 = Card('Kaladin', 'Air', 156, 2, 0)

# create a deck
dk = Deck()

# add the card to the deck
dk.addCard(c1)

print(dk.viewCards())
