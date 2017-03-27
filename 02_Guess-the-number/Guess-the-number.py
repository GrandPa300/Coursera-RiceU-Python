# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code

number_range = 100
random_number = 0
attempt_left = 0

# helper function to start and restart the game
def game_start():
    global number_range
    global random_number
    global attempt_left
    
    random_number = random.randrange(number_range)
    
    if number_range == 100:
        attempt_left = 7 
    elif number_range == 1000:
        attempt_left = 10
    elif number_range == 10000:
        attempt_left = 20
    
    print "New Game! The range is from 0 to " + str(number_range) + ". Good Luck!"
    print "Number of remaining guess is: " + str(attempt_left) + ".\n"
    pass

# define event handlers for control panel
# button that changes range to range [0,100) and restarts
def range100():
    global number_range
    number_range = 100
    game_start()
    pass
        

# button that changes range to range [0,1000) and restarts
def range1000():
    global number_range
    number_range = 1000
    game_start()
    pass

# I add a [0,10000) range as the altra-hard mode
def range10000():
    global number_range
    number_range = 10000
    game_start()
    pass

        
# main game logic goes here
def guess(input):
    global attempt_left
    attempt_left = attempt_left - 1
    input = int(input)
    
    print "You guessed: " + str(input) +"."
    print "Number of remaining guesses is " + str(attempt_left)
       
    # There are other ways to realize this logic, refer to github
    
    if input == random_number and attempt_left >= 0:
        print "This is correct! You Win!\n"
        game_start()
        return   
    elif input > random_number and attempt_left > 0:
        print "Your guess is too high!\n"
        pass    
    elif input < random_number and attempt_left > 0:
        print "Your guess is too low!\n"
        pass
    else:
        print "Game Over! You failed to guess the number!"
        print "-------- The Secert Number is "+str(random_number)+" --------- \n"
        game_start()
        return
    

# create frame
frame = simplegui.create_frame("Mini Project 2: Guess the Number!",200,200)
frame.set_canvas_background('Lightgray')

# register event handlers for control elements
frame.add_button("Esay: Range 0- 100",range100, 200)
frame.add_button("Normal: Range 0- 1000",range1000, 200)
frame.add_button("Hard: Range 0- 10000",range10000, 200)
frame.add_input("Enter Your Guess",guess, 200)

# call new_game and start frame
game_start()
frame.start()


# always remember to check your completed program against the grading rubric