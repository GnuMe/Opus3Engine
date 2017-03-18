#!/usr/bin/env python
import random
from sys import argv
script = argv
location='~'
prompt=user_name+'@opus3console:'+location+"$ "
print "What's your name?"
raw_input("pre@opus3console:pre$")
print "Hello, %s. Welcome to %s." % (user_name, script)
print "Where do you live, %s?" % user_name
lives= raw_input(prompt)
def default_game()
    roomx=0
    roomy=0
    roomxmax=2
    roomxmin=-2
    roomymax=roomxmax
    roomymin=roomxmin
    char_hp=20
    char_atk_min=1
    char_atk_max=5
    char_atk_divisor=1
    char_def_min=0
    char_def_max=2
    char_def_divisor=2
    world="Sunriseland"
default(game)
print "Welcome to the world of %s" % world
def opus3_engine():
    validDirection=False
    while validDirection=False
        print """
        w: up
        a: left
        s: down
        d: right
        Follow command with ENTER
        """
        direction=raw_input(prompt)
        location=roomx+','+roomy
        if direction == w:
            if roomx >= roomxmin and roomx <= roomxmax:
            roomx=roomx+1
            validDirection=True
        elif direction == a:
            roomx=roomx-1
            validDirection=True
        elif direction == s:
            roomy=roomy-1
            validDirection=True
        elif direction == d:
            roomy=roomy+1
            validDirection=True
        else:
            print "Invalid."
    location=roomx+','+roomy
    
        
