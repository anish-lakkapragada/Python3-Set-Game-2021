'''
Names: Agastya Pawate and Advaita Guruprasad 

Snapshot #1: Finished everything except playRound(), which is still pending and will hopefully be done by Friday...

'''
import re
from card import Card
from stack_of_cards import StackOfCards
from player import Player

class SetStack(StackOfCards):
    def isSet(self):
        #self.size = size
        #self.col 
        c1 = self.getCard(0)
        c2 = self.getCard(1)
        c3 = self.getCard(2)
        if valid(c1.getValueOf('COLOR'), c2.getValueOf('COLOR'), c3.getValueOf('COLOR')) and valid(c1.getValueOf('COUNT'), c2.getValueOf('COUNT'), c3.getValueOf('COUNT')) and valid(c1.getValueOf('SHAPE'), c2.getValueOf('SHAPE'), c3.getValueOf('SHAPE')) and valid(c1.getValueOf('VALUE'), c2.getValueOf('VALUE'), c3.getValueOf('VALUE')) and self.size() == 3:
            return True
        else:
            return False
    def displayInRows(self):
        titles = ['A', 'B', 'C']
        whereiscard = 0
        for x in range(4):
            print("   ", x, end='    ')
        print()
        for i in range(3):
            print(titles[i], end=' ')
            for y in range(4):
                print(self.getCard(whereiscard), end='    ')
                whereiscard += 1
            print()

    
# Input:
#   deck - SetStack which is the deck to draw new cards from
#   upCards - SetStack that are face up
#   players - list of Player
# Return boolean: True to continue game, False to end game

def valid(in_one, in_two, in_three):
    if in_one == in_two and in_two == in_three:
        return True
    elif in_one != in_two and in_two != in_three and in_three != in_one:
        return True
    else:
        return False

# position logic
#    1    2    3    4
# A  0    1    2    3
# B  4    5    6    7
# C  8    9    10   11

def converttoreference(pos, stack):
  letters = ["a", "b", "c"]
  letter_indx = pos//(stack.size()//3)
  number = pos%(stack.size()//3) + 1
  reference = letters[letter_indx] + str(number)
  return reference
  

def playRound(deck, upCards, players):
  score = 0 
  currentSet = SetStack() 
  print("A new game has begun!") 
  for x in range(len(players)): 
    print("Hello, {}!".format(players[x].getName())) 
    upCards.displayInRows() 
    isSet = input("Can you find a set? (y/n) ")
    if isSet == "y":
      description = input("What is the set? ")
      desc_one = description[0:2]
      desc_two = description[3:5]
      desc_three = description[6:8]
      describeSet = [desc_one, desc_two, desc_three]
      pos = 0
      while pos < upCards.size():
        if (str(describeSet[0]) == converttoreference(pos, upCards)) or (str(describeSet[1]) == converttoreference(pos, upCards)) or (str(describeSet[2]) == converttoreference(pos, upCards)):
          currentSet.add(upCards.getCard(pos))
          pos += 1
        else:
          pos += 1
     
        
      
      if currentSet.isSet():
        print(currentSet, end="")
        print("This is a set!")
        score = score + 1
      else:
        print("Sorry, that isn't a set.")
    elif isSet == "n":
      if upCards.size() < 21:
        for x in range(3):
          upCards.add(deck.deal())
      else:
        print("In 21 cards, there's a 100% chance of finding a set. Find a set already!")
    return False

# Input:
#   deck - SetStack which is the deck to draw new cards from
#   players - list of Player
# No return value
def playSetGame(deck, players):
    upCards = SetStack()
    keep_playing = True
    for i in range(12):
        upCards.add(deck.deal()) # deal 12 cards from the deck
    while keep_playing:
        keep_playing = playRound(deck, upCards, players)  # repeatedly call playRound until the game is over
   
def play():
    # get player(s) name
    name = input("What is your name? ")
    player = Player(name)
    players = [player]
    # make deck & shuffle it
    cards = SetStack()
    for inp_one in range(3):
        for inp_two in range(3):
            for inp_three in range(3):
                for inp_four in range(3):
                    cards.add(Card(inp_one, inp_two, inp_three, inp_four))
    cards.shuffle()
    playSetGame(cards, players) # call playSetGame
    choice = input("Do you want to play again? (y/n) ") # Play again? (first time around)
    while choice == 'y': # While the choice is yes (also catches the "n" like an if statement)
        playSetGame(cards, players) # Keep playing games
        choice = input("Do you want to play again? (y/n) ") # Play again?
    return # exit game

def main():
    # sample code using Card, StackOfCards, Player classes
    c = Card(0, 1, 2, 0)				# make a Set card with attributes of
							# value: 0
							# color: 1
							# count: 2
							# shape: 0
    print(c)						# will print out x x x

    deck = SetStack()  				# make a stack of cards
    deck.add(c)						# add the card to the deck
    deck.add(Card(1, 2, 2, 2))		# add another card to the deck
    deck.add(Card(2, 0, 2, 1))		# add another card to the deck
    print(deck)						# should print three cards
    print(deck.isSet())			# should print True
    #deck.displayInRows()


    player = Player("Mark") 		# make a player called Mark
    players = [ player ]
    play() 
    
if __name__ == "__main__":
    main()
