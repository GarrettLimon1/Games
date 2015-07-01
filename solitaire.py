import numpy as np
import time

"""
Solitaire game.
"""

cardlist = [0, 'AH', 'AS', 'AD', 'AC', 
            '2H', '2S', '2D', '2C', 
            '3H', '3S', '3D', '3C', 
            '4H', '4S', '4D', '4C', 
            '5H', '5S', '5D', '5C', 
            '6H', '6S', '6D', '6C', 
            '7H', '7S', '7D', '7C', 
            '8H', '8S', '8D', '8C', 
            '9H', '9S', '9D', '9C', 
            '10H', '10S', '10D', '10C', 
            'JH', 'JS', 'JD', 'JC', 
            'QH', 'QS', 'QD', 'QC', 
            'KH', 'KS', 'KD', 'KC']

class Solitaire:

    def __init__(self):
        self.columns = {1:[],2:[],3:[],4:[],
                        5:[],6:[],7:[]}
        self.used = []
        self.stacks = {'H':[],'S':[],'D':[],'C':[]}
        self.deck = []
        self._start()


    def _start(self):
        for i in range(1,8):
            self._dealcolumns(i)
            print 'XX', str(self.columns[i][len(self.columns[i])-1])
        #print self.columns
        for k in range(1,53):
            if k not in self.used:
                self.deck.append(k)
        #print self.deck
        print ("")
        print ("Start!")
        self.starttime = time.time()


    def move(self, oldcolumn, card, newcolumn):
        indx = self.columns[oldcolumn].index(card)
        prevlen = len(self.columns[newcolumn])
        for j in range(indx, len(self.columns[oldcolumn])):
            self.columns[newcolumn].append(self.columns[oldcolumn][j])
            self.columns[oldcolumn].pop(j)
        for i in range(1,8):
            if i == newcolumn:
                for k in range(prevlen-1, len(self.columns[newcolumn])):
                    if k == len(self.columns[newcolumn])-1:
                        print (str(self.columns[i][k]))
                    else:
                        print 'XX', str(self.columns[i][k]),
            elif len(self.columns[i]) == 0:
                print '(empty)'
            else:
                print 'XX', str(self.columns[i][len(self.columns[i])-1])
        #BUG: move() doesnt print out cards from previous move()




    def flip(self):
        print ("This will turn over three cards from deck")


    def stack(self, column, card, suit):
        print ("This will stack each suit's stacks")


    def _dealcolumns(self, column):
        for j in range(column):
            self._dealcolumn(column)


    def _dealcolumn(self, column):
        card = np.random.randint(1,53)
        if card not in self.used:
            self.columns[column].append(cardlist[card])
            self.used.append(card)
        else:
            self._dealcolumn(column)


