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
global enemy
global enem_hp
global enem_atk_divisor
global enem_atk_max
global enem_atk_min
global enem_def_divisor
global enem_def_max 
global enem_def_min
global world
global gotKey
global koboldDefeated
global gameDone
#Reference fight script
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
    gameDone=True 
