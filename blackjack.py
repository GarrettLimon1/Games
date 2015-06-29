import numpy as np

"""
This is an interactive Blackjack game.
Directions:
    Load the module into player's interactive 
    python command line.
    Create an instance variable of the game 
        i.e. game = bj.blackjack()
        This will automatically deal the game.
    To hit, use instance method 'hit()'
        i.e. game.hit()
    To stay, use instance method 'stay()'
"""


class blackjack:

    def __init__(self):
        '''Create the blackjack object,
        initiallize the variables.'''
        self.used = []
        self.playercards = []
        self.dealercards = []
        self.score = {'player':0, 'dealer':0}
        self.plyrace = False 
        self.dlrace = False
        #ace booleans to keep track of high aces 
        #False if ace is low (1 point) or non existant
        #True if ace is high (11 points)
        self._start()



    def hit(self): 
        '''Method that deals a new card to the player 
        if the plyaer chooses to hit.'''
        self._deal('player')
        #print self.playercards, self.score['player']
        #print self.used

        #print out the resulting hand:
        print ""
        print "Your hand:",
        for i in range(len(self.playercards)):
            if i == len(self.playercards)-1:
                print self.playercards[i]
            else:
                print(self.playercards[i]+','),
        print ("Your score: "+
               str(self.score['player']))
        print ""
        if self.score['player'] > 21: #if the player busts
            print "BUST!"
            print "You lost"
            print "Better luck next time..."
        else: #if the player is safe
            print "hit or stay?"



    def stay(self):
        '''Method that tells the program the player is 
        staying with his or her hand.'''
        print ""
        print "Your hand:", #prints the player's hand to screen
        for i in range(len(self.playercards)):
            if i == len(self.playercards)-1:
                print self.playercards[i]
            else:
                print(self.playercards[i]+','),
        print "Your score:", str(self.score['player'])
        self._dealerturn()
        print ""
        print "Dealer's hand:",
        for i in range(len(self.dealercards)):
            if i == len(self.dealercards)-1:
                print self.dealercards[i]
            else:
                print(self.dealercards[i]+','),
        if self.score['dealer']>21: #If the delaer busts
            print ""
            print "Dealer Busted!"
            print "Congrats, you won!"
        else:
            print "Dealer score:", str(self.score['dealer'])
            print ""
            #Final score 
            if self.score['player'] > self.score['dealer']:
                print "You Won!"
            elif self.score['player'] < self.score['dealer']:
                print "Dealer Won!"
                print "Better luck next time..."
            else:
                print("Tied! looks like you'll have to"+
                      " play again!")


    def _dealerturn(self):
        '''Plays the dealer's turn''' 
        #Dealer hits on everything 16 or less.
        while self.score['dealer'] <= 16:
            self._deal('dealer')
#        if self.dlrace == True and self.score['dealer'] == 17:
#            self._deal('dealer')
            

    def _start(self):
        '''This starts the game, deals the player and 
        dealer their first two cards, in proper 
        dealing order.'''
        for i in range(2):
            self._deal('player')
            self._deal('dealer')
        #print self.playercards, self.score['player']
        #print self.dealercards, self.score['dealer']
        #print self.used
        print ""
        print "Your hand:",
        for i in range(len(self.playercards)):
            if i == len(self.playercards)-1:
                print self.playercards[i]
            else:
                print(self.playercards[i]+','),
        print "Your score:", self.score['player']
        print ""
        print "Dealer's hand: XX,", self.dealercards[1]
        print ""
        print "hit or stay?"



    def _deal(self, person):
        '''Creates the card variable for each person's.'''
        card = np.random.randint(1,53)
        if card not in self.used:
            self.used.append(card) 
            #appends all cards to a list of used cards 
            #so that the cards do not repeat.
            self._cardattributes(card, person)
            #sets the card's value, number, and suite
        else:
            self._deal(person)
            #picks a new card if card has been used



    def _scorecard(self, cardvalue, person):
        '''Scores each card and adds the card's value to
        the player's score.'''
        if person == 'player':
            if self.plyrace == False: #If the ace is low
                self.score[person] += cardvalue
            else: #If the ace is high
                if self.score[person] + cardvalue <= 21:
                    #keep ace high
                    self.score[person] += cardvalue
                else:
                    #make the ace low!
                    self.score[person] += (cardvalue -10)
                    self.plyrace = False
        else: #Same for dealer
            if self.dlrace == False:
                self.score[person] += cardvalue
            else:
                if self.score[person] + cardvalue <= 21:
                    self.score[person] += cardvalue
                else:
                    self.score[person] += (cardvalue -10)
                    self.dlrace = False


    def _namecard(self, person, cardsuit, cardnum):
        '''Appends a list of each player's cards's name
        i.e. KS (king of spades)'''
        if person == 'player':
            self.playercards.append(cardnum+cardsuit)
        else:
            self.dealercards.append(cardnum+cardsuit)



    def _cardattributes(self, card, person):
        '''Gives each card its attributes, the card's value,
        the card's number, and the card's suit'''
        suits = ['C', 'S', 'H', 'D']
        if card <= 4:
            cardnum = '2'
            cardvalue = 2
            for i in range(4):
                if card == i+1:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 8:
            cardnum = '3'
            cardvalue = 3
            for i in range(4):
                if card == i+5:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 12:
            cardnum = '4'
            cardvalue = 4
            for i in range(4):
                if card == i+9:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 16:
            cardnum = '5'
            cardvalue = 5
            for i in range(4):
                if card == i+13:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 20:
            cardnum = '6'
            cardvalue = 6
            for i in range(4):
                if card == i+17:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 24:
            cardnum = '7'
            cardvalue = 7
            for i in range(4):
                if card == i+21:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 28:
            cardnum = '8'
            cardvalue = 8
            for i in range(4):
                if card == i+25:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 32:
            cardnum = '9'
            cardvalue = 9
            for i in range(4):
                if card == i+29:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 36:
            cardnum = '10'
            cardvalue = 10
            for i in range(4):
                if card == i+33:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 40:
            cardnum = 'J'
            cardvalue = 10
            for i in range(4):
                if card == i+37:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 44:
            cardnum = 'Q'
            cardvalue = 10
            for i in range(4):
                if card == i+41:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 48:
            cardnum = 'K'
            cardvalue = 10
            for i in range(4):
                if card == i+45:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        else: #Aces are tricky
            if person == 'player':
                cardnum = 'A'
                if self.score[person] + 11 > 21:
                    cardvalue = 1
                else:
                    cardvalue = 11 
                    self.plyrace = True #Ace becomes high!
                for i in range(4):
                    if card == i+49:
                        cardsuit = suits[i]
                self._scorecard(cardvalue, person)
                self._namecard(person, cardsuit, cardnum)
            else:
                cardnum = 'A'
                if self.score[person] + 11 > 21:
                    cardvalue = 1
                else:
                    cardvalue = 11
                    self.dlrace = True 
                for i in range(4):
                    if card == i+49:
                        cardsuit = suits[i]
                self._scorecard(cardvalue, person)
                self._namecard(person, cardsuit, cardnum)




if __name__ == "__main__":
    print "Testing..."
    
    playerwins = 0.
    dealerwins = 0.
    ties = 0.
    rounds = 1000
    for i in range(rounds):
        print "Game ",i+1
        test = blackjack()
        while test.score['player'] <= 16:
            test.hit()
        if test.score['player'] <= 21:
            test.stay()
            
        print ""
        if test.score['player'] <= 21 and test.score['dealer'] <= 21:
            if test.score['player'] > test.score['dealer']:
                playerwins += 1.
            elif test.score['player'] < test.score['dealer']:
                dealerwins += 1.
            else:
                ties += 1.
        if test.score['player'] > 21:
            dealerwins += 1
        elif test.score['dealer'] > 21:
            playerwins += 1

    style = 'Soft17'
    playerresults = ("Player: " + str(playerwins) + ", " + 
           str(100.*playerwins/rounds) + "%") 
    dealerresults = ("Dealer: " + str(dealerwins) + ", " + 
           str(100.*dealerwins/rounds)+ "%")
    numberofties =  ("Ties: " + str(ties) + ", " + 
           str(100.*ties/rounds) + "%")

    file = open('./analysis/'+style+'_'+str(rounds)+'.dat', 'w')
    file.write('Results of 1000 games: \n\n' + playerresults + 
               '\n\n' +dealerresults + '\n\n' + numberofties)
