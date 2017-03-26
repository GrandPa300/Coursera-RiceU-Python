# Mini Project 1
# Rock-paper-scissors-lizard-Spock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    # fill in your code below
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    return name

    # convert number to a name using if/elfi/else
    #don't forget to return the reslut!

def name_to_number(name):
    # fill in your code below
    
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    return number 

    # convert number to a name using if/elfi/else
    #don't forget to return the reslut!

def rpsls(name): 
    # fill in your code below
    player_number = name_to_number(name)
    comp_number = random.randrange(4)
    print "Player chooses " + name
    print "Computer chooses " + number_to_name(comp_number)
    
    difference = (player_number - comp_number)%5
    #print player_number
    #print comp_number
    #print difference
    print "=============="
    if difference > 2:
        print "Computer wins!"
    elif difference == 0:
        print "Player and Computer ties!"
    else:
        print "Player wins!"
    print "=============="
    print ""
        

    # convert name to player_number using name_to_number
    # compute random guess for comp_number using random.randrange()
    # compute difference of player_number and comp_number modulo five
    # use if/elif/else to determine winner
    # convert comp_number to name using number_to_name
    # print results
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")