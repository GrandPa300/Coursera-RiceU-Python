# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949 x 392 - source: jftiz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image\
             ("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image\
            ("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize global variables
in_play = False
#outcome = ""
dealer_score = 0
player_score = 0 

# define globals for cards
SUITS = ('C','S','H','D')
RANKS = ('A','2','3','4','5','6','7','8','9','T','J','Q','K')
VALUES = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,\
          '9':9,'T':10,'J':10,'Q':10,'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else: 
            self.suit = None
            self.rank = None

    def __str__(self):
        return self.suit + self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                         CARD_SIZE)

# define hand class
class Hand:

    def __init__(self):
        self.hand = []

    def __str__(self):
        result = ''
        for card in self.hand:
            result += ' ' + str(card)
        return "Hand contains: " + result

    def add_card(self, card):
        self.hand.append(card)
    
    # count aces as 1, if the hand has an ace, then add 10 to hand value if it does not bust.
    def get_value(self):
        value = 0
        contain_ace = False
        
        for card in self.hand:
            rank = card.get_rank()
            value += VALUES[rank] 
            
            if rank == 'A':
                contain_ace = True  

        if contain_ace and value <= 11:
            value += 10
            
        return value
    
    def bust_chk(self):       
        if self.get_value() > 21:
            return True
        else:
            return False
    
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 80

# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        result = ''
        for card in self.deck:          
            result += ' ' + str(card)
        return "Full Deck Conatins: " + result[0:39]  + '\n' +\
               "                    " + result[39:78] + '\n' +\
               "                    " + result[78:117]+ '\n' +\
               "                    " + result[117:156]
    
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_card(self):
        return self.deck.pop(0)

# define event handlers for buttons
def deal():
    global outcome, in_play, dealer_score,player_hand, dealer_hand, deck
    
    if in_play:
        outcome = 'Player Lost Because of Re-deal! New Deal?'
        in_play = False
        dealer_score += 1
        print outcome
        
    else:
        outcome = 'Hit or Stand?'
        deck = Deck()
        deck.shuffle()        
        player_hand = Hand()
        dealer_hand = Hand()
        
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        
        in_play = True
        
        print "---------------------"
        print "Player %s" % player_hand
        print "Dealer %s" % str(dealer_hand)[0:16]+ "?? " \
                          + str(dealer_hand)[19:]
        print outcome
    
def hit():
    global in_play, dealer_score, outcome
    
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        print "Player %s" % player_hand
    
        # if busted, assign an message to outcome and update in_play and score
        if player_hand.bust_chk() == True:
            in_play = False
            dealer_score += 1
            outcome = 'Player Busted! New Deal?'
            print outcome
        else:
            print outcome

def stand():
    global in_play, outcome, player_score, dealer_score

    # if hand is in play, repeatedly hit dealer untill his hand has value 17 or more
    if in_play:
        print "Player Stand!"
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            
        print "Dealer %s" % dealer_hand    
            
    # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21:
            in_play = False
            outcome = 'Dealer Busted! Player Win! New Deal?'
            player_score += 1
        
        else: 
            if dealer_hand.get_value() >= player_hand.get_value():
                in_play = False
                outcome = 'Dealer Win! New Deal?'
                dealer_score += 1
            else:
                in_play = False
                outcome = 'Player Win! New Deal?'
                player_score += 1
        
        print outcome
        print '---------------------'

# draw handler
def draw(canvas):
    canvas.draw_text('Rice Casino Blackjack',[180,30],30, 'White')
    canvas.draw_text(outcome, [30,80],25,'White')
    canvas.draw_text(('Dealer: '+ str(dealer_score)), [30,150],20,'White')
    dealer_hand.draw(canvas,[105, 180])
    canvas.draw_text(('Player: '+ str(player_score)), [30,320],20,'White')
    player_hand.draw(canvas,[105, 350])
    
    if in_play:
        canvas.draw_image(card_back,CARD_BACK_CENTER, CARD_BACK_SIZE,\
                                    [105 + CARD_CENTER[0], 180 + CARD_CENTER[1]],\
                                    CARD_BACK_SIZE)
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# start the frame
frame.start()
deal()