import openpyxl


# define the card
class Card:

    # The number of cards in the deck
    numCards = 0

    def __init__(self, theName, theType, theHP, theMoves, isShiny):
        self.name = theName
        self.type = theType
        self.HP = theHP
        self.moves = theMoves
        self.Shiny = isShiny
        Card.numCards += 1  # increment the number of cards by 1
        print('You add the card {self.name} to the deck'.format(self=self))

    def __str__(self):
        return 'name: {self.name}, type: {self.type}, HP: {self.HP}, moves: {self.moves}, isShiny: {self.Shiny}.'.format(self=self)

    def __del__(self):
        Card.numCards -= 1  # decrement the number of cards by 1
        print('You removed the card {self.name} from your deck'.format(self=self))


# define the deck
class Deck:

    # define the initialiser
    def __init__(self):
        self.cards = []

    def __str__(self):
        return 'There are {Card.numCards} cards in the Deck'.format(Card=Card)
    # define method

    # importing the file
   

    # adds a card
    def addCard(self, theCard):
        self.cards.append(theCard)

    # remove a card
    def removeCard(self, theCard):
        self.cards.remove(theCard)

    # view a card details
    def viewCard(self, theCard):
        print('Name: ', theCard.name)
        print('Type: ', theCard.type)
        print('HP: ', theCard.HP)
        print('moves: ', theCard.moves)
        if theCard.Shiny:
            print('Shiny card')
        else:
            print('common card')

    # view all cards
    def viewallCards(self):
        print('view all cards')
        for c in self.cards:
            print(c)


c1 = Card('Kaladin', 'Air', 156, 2, 0)
c2 = Card('Teocrates', 'Mistral', 454, 5, 1)


# create a deck
dk = Deck()

# add the card to the deck
dk.addCard(c1)
dk.addCard(c2)

print(dk.__str__())

dk.viewCard(c2)

dk.viewallCards()

