#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from os.path import exists
location='~'
if exists('.runbefore')==False:
    with open(".runbefore","a+") as f:
        f.write("Delete this only if you want to see the license thing again")
    print """
    Do whatever you want with this software. Why the hell would I care?
    """
print "What's your name?"
user_name=raw_input("pre@opus3console:pre$ ")
prompt=user_name+'@opus3console:'+location+"$ "
def gameinit():
    exec(open('o3gameinit.py').read(), globals())
gameinit()
def fight():
    global roomx
    global roomy
    global roomxmax
    global roomxmin
    global roomymax
    global roomymin
    global char_hp
    global char_atk_divisor
    global char_atk_max
    global char_atk_min
    global char_def_divisor
    global char_def_max
    global char_def_min
    global enemy
    global enem_hp
    global enem_atk_divisor
    global enem_atk_max
    global enem_atk_min
    global enem_def_divisor
    global enem_def_max
    global enem_def_min
    global world
    try:
        print "You encountered a %s" % enemy
    except:
        print "An error occured. Enemy name set to fallback value."
        enemy = "Nameless One"
        print "You encountered a Nameless One!"
    try:
        print "%s has %d HP, and %d to %d attack." % (enemy, enem_hp,enem_atk_min/enem_atk_divisor,enem_atk_max/enem_atk_divisor)
    except:
        print "An error occured. Enemy stats were set to fallback values.."
        enem_hp=char_hp
        enem_atk_min=char_atk_min
        enem_atk_max=char_atk_max
        enem_atk_divisor=char_atk_divisor
        enem_def_divisor=char_def_divisor
        enem_def_max=char_def_max
        enem_def_min=0
        print "Nameless One has 20 HP, 1 to 5 attack, and 0 to 1 defense."
    firstturn=random.randint(0,1)
    while char_hp >= 1 and enem_hp >= 1:
        if firstturn==0:
            enem_hp=enem_hp-(random.randint(char_atk_min, char_atk_max)/char_atk_divisor)
            char_hp=char_hp-(random.randint(enem_atk_min, enem_atk_max)/enem_atk_divisor)
        else:
            char_hp=char_hp-(random.randint(enem_atk_min, enem_atk_max)/enem_atk_divisor)
            enem_hp=enem_hp-(random.randint(char_atk_min, char_atk_max)/char_atk_divisor)
    if char_hp <=1:
        print "You lose. %s lives with %d HP remaining." % (enemy, enem_hp)
    else:
        print "You win, with %d HP remaining." % char_hp
def coordOptions():
    exec(open('o3coordoptions.py').read(), globals())
print "Welcome to the world of %s" % world
def opus3_engine():
    global roomx
    global roomy
    global roomxmax
    global roomxmin
    global roomymax
    global roomymin
    global char_hp
    global char_atk_divisor
    global char_atk_max
    global char_atk_min
    global char_def_divisor
    global char_def_max
    global world
    validDirection=False
    #FIXME: Use coordinate-specific variables.
    isOn=True
    while char_hp>=1 and gameDone == False:
        print "HP: %d" % char_hp
        print """
        w: up
        a: left
        s: down
        d: right
        Follow command with ENTER
        """
        direction=raw_input(user_name+" in "+world+"("+str(roomx)+','+str(roomy)+")$ ")
        if direction == "d":
            if roomx <= roomxmax:
                roomx=roomx+1
                validDirection=True
            else:
                print "You slammed yourself into a wall."
                char_hp=char_hp-1
        elif direction == "a":
            if roomx >= roomxmin:
                roomx=roomx-1
                validDirection=True
            else:
                print "You slammed yourself into a wall."
                char_hp=char_hp-1
        elif direction == "s":
            if roomy >= roomymin:
                roomy=roomy-1
                validDirection=True
            else:
                print "You slammed yourself into a wall."
                char_hp=char_hp-1
        elif direction == "w":
            if roomy <= roomymax:
                roomy=roomy+1
                validDirection=True
            else:
                print "You slammed yourself into a wall."
                char_hp=char_hp-1
        else:
            print "Invalid."
    if char_hp <= 0:
        print "You died."
    else:
        print "You won!"
opus3_engine()
