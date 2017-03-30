# implementation of card game - Memory

import simplegui
import random

# Initialize global variables

NUMBERS = range(8)

status = 0
moves = 0
choice = 0
card1 = 0
card2 = 0

flip = []
memory_list = []

# helper function to initialize globals
def init():
    global status, moves, flip, memory_list
    status = 0
    moves = 0
    label.set_text("Moves: " + str(moves))
    
    # flip initial status False for each card
    flip = [False for n in range(16)]
    
    # shuffle memory list at beginning of the game
    memory_list = NUMBERS + NUMBERS   
    random.shuffle(memory_list)    

# define event handlers
def mouseclick(pos):
    global flip, status, moves, card1, card2
            
    card = pos[0]//50
    choice = memory_list[card]
    
    if flip[card]:
        pass
    else:
        
        if status == 0:
            status = 1
            moves += 1
            flip[card] = True
            card1 = card
            
        elif status == 1:
            if choice == memory_list[card1]:
                flip[card] = True
                status = 0
            else:
                flip[card] = True
                card2 = card
                status = 2
            
        elif status == 2:
            if choice == memory_list[card2]:
                flip[card] = True
                flip[card1] = False
                status = 0
                
            else:
                flip[card] = True
                flip[card1] = False
                flip[card2] = False
                card1 = card
                moves +=1
                status = 1
        label.set_text("Moves: " + str(moves))

            
    
# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(16):
        if flip[i]:
            canvas.draw_polygon([(i*50,0),((i+1)*50,0),((i+1)*50,100),(i*50,100),],\
                            2,'White','Green')
            canvas.draw_text(str(memory_list[i]), [i*50+20,60],30,"White")
        else:
            canvas.draw_polygon([(i*50,0),((i+1)*50,0),((i+1)*50,100),(i*50,100),],\
                            2,'White','Green')
            canvas.draw_text('?',[i*50+20,60],30,"White")
    
# create frame and add a button and labels
frame = simplegui.create_frame('Memory', 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves: 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()