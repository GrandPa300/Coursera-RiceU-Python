# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def init():

# define event handlers
def mouseclick(pos):
    
# create frame and add a button and labels
frame = simplegui.create_frame('Memory', 800, 100)
frame.add_button("Restart", init)
l = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()