# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles

WIDTH = 600
HEIGHT = 400
BALL_RAD = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PADDLE_VEL = 8.0

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_rad = 10
ball_vel = [0 , 0]

paddle1_pos = [HALF_PAD_WIDTH * 1.0, HEIGHT / 2.0]
paddle1_vel = [0.0 , 0.0]
paddle2_pos = [(WIDTH - HALF_PAD_WIDTH) * 1.0, HEIGHT / 2.0]
paddle2_vel = [0.0 , 0.0]


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(direction):
    global ball_pos, ball_val # there are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    random_num = [-4,-3,-2,2,3,-4]
    ball_vel[0] = random.randrange(2,4)
    ball_vel[1] = random.choice(random_num)
    # Right = Ture, and Left = True
    if direction == True:
        ball_vel[0] = -1* ball_vel[0]
    
    pass

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are floats
    global score1, score2 # these are ints
    paddle1_pos = [HALF_PAD_WIDTH * 1.0, HEIGHT / 2.0]
    paddle2_pos = [(WIDTH - HALF_PAD_WIDTH) * 1.0, HEIGHT / 2.0]
    paddle1_vel = [0.0 , 0.0]
    paddle2_vel = [0.0 , 0.0]
    score1 = 0  
    score2 = 0
    ball_init(0)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_vel
    
    # update paddle's vertical position, keep paddle on the screen
    # accerelation of paddle = 0.1 to make movement smoother
    
    if paddle1_pos[1] >= HALF_PAD_HEIGHT and paddle1_vel[1] < 0: 
        paddle1_vel[1] -= 0.1
        paddle1_pos[1] += paddle1_vel[1]
    elif paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT - 1 and paddle1_vel[1] > 0:
        paddle1_vel[1] += 0.1
        paddle1_pos[1] += paddle1_vel[1]

    if paddle2_pos[1] >= HALF_PAD_HEIGHT and paddle2_vel[1] < 0:
        paddle2_vel[1] -= 0.1
        paddle2_pos[1] += paddle2_vel[1]
    elif paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT - 1 and paddle2_vel[1] > 0:
        paddle2_vel[1] += 0.1
        paddle2_pos[1] += paddle2_vel[1]
   
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 2, "Lime")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 2, "Lime")
    c.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 2, "Lime")
    c.draw_circle([WIDTH/2, HEIGHT/2], 60, 2, "Lime")
    
    # draw paddles

    c.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT], \
                [paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], 8, "Lime")
    c.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT], \
                [paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], 8, "Lime")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collisoin and reflection
    if ball_pos[0] <= PAD_WIDTH + ball_rad:
        if (ball_pos[1] > paddle1_pos[1] - HALF_PAD_HEIGHT - ball_rad and\
            ball_pos[1] < paddle1_pos[1] + HALF_PAD_HEIGHT + ball_rad):
            ball_vel[0] *= -1.1
        else:
            score2 += 1
            ball_init(False)
            
    elif ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - ball_rad:
        if (ball_pos[1] > paddle2_pos[1] - HALF_PAD_HEIGHT - ball_rad and\
            ball_pos[1] < paddle2_pos[1] + HALF_PAD_HEIGHT + ball_rad):
            ball_vel[0] *= -1.1
        else:
            score1 += 1
            ball_init(True)
                       
    if ball_pos[1] <= ball_rad or ball_pos[1] >= (HEIGHT - ball_rad):
        ball_vel[1] = -1* ball_vel[1]
        
    # draw ball and scores
    c.draw_circle(ball_pos, ball_rad, 2, "Lime","Lime")
    c.draw_text("Player1: " + str(score1), [30,350],20, 'Lime')
    c.draw_text("Player2: " + str(score2), [500,50],20, 'Lime')
    
def keydown(key):
    # Player 1
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] = -PADDLE_VEL
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] = PADDLE_VEL
        
    # Player 2
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] = -PADDLE_VEL
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] = PADDLE_VEL
        
def keyup(key):
    # Player 1
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] = 0.0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] = 0.0

    # Player 2
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] = 0.0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] = 0.0

# create frame
frame = simplegui.create_frame("Pong!", WIDTH, HEIGHT)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

# start frame
init()
frame.start()