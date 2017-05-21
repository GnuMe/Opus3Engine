import opus3
opus3.location='~'    
opus3.user_name="idkwhatyournameis"
opus3.prompt=opus3.user_name+'@opus3console:'+opus3.location+"$ "
gameDone=False
opus3.roomx=0
opus3.roomy=0
opus3.roomxmax=2
opus3.roomxmin=-2
opus3.roomymax=opus3.roomxmax
opus3.roomymin=opus3.roomxmin
opus3.char_hp=20
opus3.char_atk_min=1
opus3.char_atk_max=5
opus3.char_atk_divisor=1
opus3.char_def_min=0
opus3.char_def_max=2
opus3.char_def_divisor=2
opus3.world="Opus 3 Demo"
#game specific variables
koboldDefeated=False
gotKey=False
opus3.initprompt()
while opus3.isOn==True:
    opus3.main()
    if validDirection=True:
        if roomx==1 and roomy==0 and koboldDefeated==False:
        enemy="Kobold"
        enem_hp=10
        enem_atk_min=5
        enem_atk_max=8
        enem_atk_divisor=2
        enem_def_min=0
        enem_def_min=2
        enem_def_divisor=1
        fight()
        koboldDefeated=True
    #Reference quest
    if roomx==0 and roomy==-3 and gotKey==False:
        print "You found the key to the Warden's Chest!"
        gotKey=True
    if roomx==3 and roomy==2 and gotKey==True:
        print "As you place the key into the keyhole, the dungeon wall"
        print "crumbles and the town of Demolia is in front of you."
        opus3.isOn=False
