#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from os.path import exists
location='~'
#FIXME: Make this firstrun only and allow multiple inputs. Superlow priority.
#This is the suggested way by the FSF to show
#GPL info, pythonified and modified slightly.
if exists('.runbefore')==False:
    with open(".runbefore","a+") as f:
        f.write("Delete this only if you want to see the license thing again")
    print """
    Opus 3 'Engine' Copyright (C) 2017  Ivan Stanton
    This program comes with ABSOLUTELY NO WARRANTY; for details type 'w'.
    This is doubly free (as in freedom and price) software, and you are 
    welcome to redistribute it if it remains so; type 'c' for details (
    beware - wall of text!).
    """
    license_option=raw_input("pre@opus3console:pre$ ")
    if license_option == "w":
        print """
    THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY 
    APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT 
    HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY 
    OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, 
    THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
    PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM 
    IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF 
    ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
    """
    elif license_option == "c":
        print """
    CONVEYING VERBATIM COPIES

    You may convey verbatim copies of the Program's source code as you receive 
    it, in any medium, provided that you conspicuously and appropriately 
    publish on each copy an appropriate copyright notice; keep intact all 
    notices stating that this License and any non-permissive terms added in 
    accord with section 7 apply to the code; keep intact all notices of the 
    absence of any warranty; and give all recipients a copy of this License 
    along with the Program.
    
    You may charge any price or no price for each copy that you convey, and 
    you may offer support or warranty protection for a fee.

    CONVEYING MODIFIED SOURCE VERSIONS

    You may convey a work based on the Program, or the modifications to 
    produce it from the Program, in the form of source code under the terms of 
    section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified it, and  
    giving a relevant date.
    b) The work must carry prominent notices stating that it is released under 
    this License and any conditions added under section 7. This requirement 
    modifies the requirement in section 4 to “keep intact all notices”.
    c) You must license the entire work, as a whole, under this License to 
    anyone who comes into possession of a copy. This License will therefore 
    apply, along with any applicable section 7 additional terms, to the whole 
    of the work, and all its parts, regardless of how they are packaged. This 
    License gives no permission to license the work in any other way, but it 
    does not invalidate such permission if you have separately received it.
    d) If the work has interactive user interfaces, each must display 
    Appropriate Legal Notices; however, if the Program has interactive 
    interfaces that do not display Appropriate Legal Notices, your work need 
    not make them do so.
    A compilation of a covered work with other separate and independent works, 
    which are not by their nature extensions of the covered work, and which 
    are not combined with it such as to form a larger program, in or on a 
    volume of a storage or distribution medium, is called an “aggregate” if 
    the compilation and its resulting copyright are not used to limit the 
    access or legal rights of the compilation's users beyond what the 
    individual works permit. Inclusion of a covered work in an aggregate does 
    not cause this License to apply to the other parts of the aggregate.

    CONVEYING NON-SOURCE CODE

    
    You may convey a covered work in object code form under the terms of 
    sections 4 and 5, provided that you also convey the machine-readable 
    Corresponding Source under the terms of this License, in one of these 
    ways:

    a) Convey the object code in, or embodied in, a physical product 
    (including a physical distribution medium), accompanied by the 
    Corresponding Source fixed on a durable physical medium customarily used 
    for software interchange.
    b) Convey the object code in, or embodied in, a physical product 
    (including a physical distribution medium), accompanied by a written 
    offer, valid for at least three years and valid for as long as you offer 
    spare parts or customer support for that product model, to give anyone who 
    possesses the object code either (1) a copy of the Corresponding Source 
    for all the software in the product that is covered by this License, on a 
    durable physical medium customarily used for software interchange, for a 
    price no more than your reasonable cost of physically performing this 
    conveying of source, or (2) access to copy the Corresponding Source from a 
    network server at no charge.
    c) Convey individual copies of the object code with a copy of the written 
    offer to provide the Corresponding Source. This alternative is allowed 
    only occasionally and noncommercially, and only if you received the object 
    code with such an offer, in accord with subsection 6b.
    d) Convey the object code by offering access from a designated place 
    (gratis or for a charge), and offer equivalent access to the Corresponding 
    Source in the same way through the same place at no further charge. You 
    need not require recipients to copy the Corresponding Source along with 
    the object code. If the place to copy the object code is a network server, 
    the Corresponding Source may be on a different server (operated by you or 
    a third party) that supports equivalent copying facilities, provided you 
    maintain clear directions next to the object code saying where to find the 
    Corresponding Source. Regardless of what server hosts the Corresponding 
    Source, you remain obligated to ensure that it is available for as long as 
    needed to satisfy these requirements.
    e) Convey the object code using peer-to-peer transmission, provided you 
    inform other peers where the object code and Corresponding Source of the 
    work are being offered to the general public at no charge under subsection 
    6d.
    A separable portion of the object code, whose source code is excluded from 
    the Corresponding Source as a System Library, need not be included in 
    conveying the object code work.

    A “User Product” is either (1) a “consumer product”, which means any 
    tangible personal property which is normally used for personal, family, or 
    household purposes, or (2) anything designed or sold for incorporation 
    into a dwelling. In determining whether a product is a consumer product, 
    doubtful cases shall be resolved in favor of coverage. For a particular 
    product received by a particular user, “normally used” refers to a typical 
    or common use of that class of product, regardless of the status of the 
    particular user or of the way in which the particular user actually uses, 
    or expects or is expected to use, the product. A product is a consumer 
    product regardless of whether the product has substantial commercial, 
    industrial or non-consumer uses, unless such uses represent the only 
    significant mode of use of the product.

    “Installation Information” for a User Product means any methods, 
    procedures, authorization keys, or other information required to install 
    and execute modified versions of a covered work in that User Product from 
    a modified version of its Corresponding Source. The information must 
    suffice to ensure that the continued functioning of the modified object 
    code is in no case prevented or interfered with solely because 
    modification has been made.

    If you convey an object code work under this section in, or with, or 
    specifically for use in, a User Product, and the conveying occurs as part 
    of a transaction in which the right of possession and use of the User 
    Product is transferred to the recipient in perpetuity or for a fixed term 
    (regardless of how the transaction is characterized), the Corresponding 
    Source conveyed under this section must be accompanied by the Installation 
    Information. But this requirement does not apply if neither you nor any 
    third party retains the ability to install modified object code on the 
    User Product (for example, the work has been installed in ROM).

    The requirement to provide Installation Information does not include a 
    requirement to continue to provide support service, warranty, or updates 
    for a work that has been modified or installed by the recipient, or for 
    the User Product in which it has been modified or installed. Access to a 
    network may be denied when the modification itself materially and 
    adversely affects the operation of the network or violates the rules and 
    protocols for communication across the network.
    
    Corresponding Source conveyed, and Installation Information provided, in 
    accord with this section must be in a format that is publicly documented \
    (and with an implementation available to the public in source code form), 
    and must require no special password or key for unpacking, reading or 
    copying.
    """
print "What's your name?"
user_name=raw_input("pre@opus3console:pre$ ")
prompt=user_name+'@opus3console:'+location+"$ "
lives= raw_input(prompt)
def gameinit():
    #FIXME: Developers should not have to define every variable as global.
    #FIXME: Add coordinate-specific variables.
    #FIXME: Allow variables to be loaded from files.
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
def fight():
    print "Nothing here yet..."
def game_coordoptions():
    print "No coordinate options set."
gameinit()
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
    while char_hp>=1:
        print "HP: %d" % char_hp
        print """
        w: up
        a: left
        s: down
        d: right
        Follow command with ENTER
        """
        direction=raw_input(user_name+world+str(roomx)+','+str(roomy)+"$ ")
        if direction == "w":
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
        elif direction == "d":
            if roomy <= roomymax:
                roomy=roomy+1
                validDirection=True
            else:
                print "You slammed yourself into a wall."
                char_hp=char_hp-1
        else:
            print "Invalid."
    print "You died."
opus3_engine()
