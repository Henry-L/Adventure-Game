#This is the final and main section of the game. This is where the player can
#explore a map to a sertain degree and ultimately fights the goblin mentioned
#in the quest. The player is allowed to take a certain number of steps before
#being attacked by said Goblin. During the fight, the player can make one of
#actions (Attack or Defend) and the damage that is dealt to and by the hero
#is partially determined by the class they chose in the introduction section.
#The Goblin is made to be weak (so weak I did not program what would happen if
#the player dies first, once again, maybe in the future). Upon defeating the
#Goblin, there is a victory screen and the game is over.

from graphics import *
from button import *
from goblin_class import *
from character_class import *
from person_class import *
import random,time

def makeSides(win): #These 4 rectangle cover up the moving map, that is their only purpose
    rec1=Rectangle(Point(-1,-1),Point(41,6))
    rec1.setFill('burlywood')
    rec1.setOutline('burlywood')
    rec1.draw(win)
    rec2=Rectangle(Point(-1,34),Point(41,41))
    rec2.setFill('burlywood')
    rec2.setOutline('burlywood')
    rec2.draw(win)
    rec3=Rectangle(Point(-1,6),Point(6,34))
    rec3.setFill('burlywood')
    rec3.setOutline('burlywood')
    rec3.draw(win)
    rec4=Rectangle(Point(34,6),Point(41,34))
    rec4.setFill('burlywood')
    rec4.setOutline('burlywood')
    rec4.draw(win)

def makeBorder(win): #The border around the moving map, just for style
    border1=Rectangle(Point(6,6),Point(34,34))
    border1.setOutline('black')
    border1.setWidth(3)
    border1.draw(win)

def makeArrows(win): #The arrows on the side that act as buttons for movement
    arrowd=Polygon(Point(18,5),Point(22,5),Point(22,3),Point(24,3),Point(20,1),Point(16,3),Point(18,3))
    arrowd.setFill('dimgray')
    arrowd.draw(win)

    arrowu=Polygon(Point(18,35),Point(22,35),Point(22,37),Point(24,37),Point(20,39),Point(16,37),Point(18,37))
    arrowu.setFill('dimgray')
    arrowu.draw(win)

    arrowl=Polygon(Point(5,22),Point(5,18),Point(3,18),Point(3,16),Point(1,20),Point(3,24),Point(3,22))
    arrowl.setFill('dimgray')
    arrowl.draw(win)

    arrowr=Polygon(Point(35,18),Point(35,22),Point(37,22),Point(37,24),Point(39,20),Point(37,16),Point(37,18))
    arrowr.setFill('dimgray')
    arrowr.draw(win)

def drawHero(win): #The circle in the center that represents the player/hero
    hero=Circle(Point(20,20),.75)
    hero.setFill('black')
    hero.draw(win)

def makeButtons(win): #The invisible buttons that are around the previously drawn arrows
    bu=Button(win,Point(20,37),4,4,'')
    bu.activate()
    bd=Button(win,Point(20,3),4,4,'')
    bd.activate()
    bl=Button(win,Point(3,20),4,4,'')
    bl.activate()
    br=Button(win,Point(37,20),4,4,'')
    br.activate()
    return bu,bd,bl,br


def movement(win,bu,bd,bl,br,horiz,vert,movenum,img): #Function that facilitates the movement of the map/hero
    #The four parameters after win are the buttons representing movement in the four directions
    #horiz and vert are numbers which track the position of the hero, both start at 0
    #movenum is the number of steps taken by hero, also starts at 0
    #img is the image that acts as the map and moves to convey movement of hero
    done=False
    while not done:
        p=win.getMouse()
        if movenum==13:
            done=True
        elif bu.clicked(p):
            movenum=movenum+1
            if vert!=10:
                vert=vert+1
                img.move(0,-1)
                done=False
            else:
                done=False
        elif bd.clicked(p):
            movenum=movenum+1
            if vert!=-10:
                vert=vert-1
                img.move(0,1)
                done=False
            else:
                done=False
        elif bl.clicked(p):
            movenum=movenum+1
            if horiz!=-26:
                horiz=horiz-1
                img.move(1,0)
                done=False
            else:
                done=False
        elif br.clicked(p):
            movenum=movenum+1
            if horiz!=26:
                horiz=horiz+1
                img.move(-1,0)
                done=False
            else:
                done=False
        else:
            done=True


def encounter(win2):
    bob=Goblin(23,3,3,0) #Goblin character which the hero fights
    enc=Text(Point(20,30),"""You are attacked
    by a Goblin!""")
    enc.setFace('papyrus')
    enc.setStyle('bold')
    enc.setSize(25)
    enc.draw(win2)
    time.sleep(1.5)
    action=Text(Point(20,17),'You must defeat him!')
    action.setStyle('bold')
    action.setFace('papyrus')
    action.setSize(20)
    action.draw(win2)
    time.sleep(1.5)
    enc.undraw()
    action.undraw()
    return bob

def att_defbuttons(win2): #Creates the buttons for the two actions available in the fight
    battack=Button(win2,Point(20,30),28,18,'')
    battack.drawButton('ATTACK',win2)
    battack.setSize(30)
    bdefend=Button(win2,Point(20,10),28,18,'')
    bdefend.drawButton('DEFEND',win2)
    bdefend.setSize(30)
    return battack, bdefend

def goblin_attack(win2,gob,hero): #An attack from the goblin
    damage_gob=gob.attack() #The damage from the goblin
    taken=Text(Point(20,11),'The goblin lunges at you, dealing %.2f damage' % (damage_gob))
    taken.setSize(15)
    taken.setFace('papyrus')
    taken.draw(win2)
    hero.changeHP(-(round(damage_gob))) #The damage is subtracted from hero's HP. Number is rounded for convenience
    time.sleep(1)
    return taken,damage_gob
    
def hero_attack_whole(win2,hero,gob): #Represents the whole turn if the hero chooses to attack
        damage_hero=hero.attack() #The damage from hero
        dealt=Text(Point(20,31),'You swing your weapon, dealing %.2f damage' % (damage_hero))
        dealt.setSize(14)
        dealt.setFace('papyrus')
        dealt.draw(win2)
        gob.changeHP(-(round(damage_hero))) #Damage subtracted from Goblin's HP
        time.sleep(1)
        taken,damage_gob=goblin_attack(win2,gob,hero) #Calling the previos function to handle goblin attack
        heroHPt, gobHPt = HP_check(win2,hero.getHP(),gob.getHP()) #Prints the HPs of both parties
#        print bob.getHP()
#        print hero.getHP()
        time.sleep(3)
        dealt.undraw() #Clears screen
        taken.undraw()
        heroHPt.undraw()
        gobHPt.undraw()

def hero_defend_whole(win2,hero,gob): #Represents the whole turn if the hero chooses to defend
    blocked_hero=hero.defend() #Amount of damage shielded
#       print blocked_hero
#       print damage_gob
    taken,damage_gob=goblin_attack(win2,gob,hero)
    block=Text(Point(20,31),'You shield yourself, blocking %.2f damage' % (blocked_hero))
    block.setSize(15)
    block.setFace('papyrus')
    block.draw(win2)
    time.sleep(1)
    if (round(blocked_hero))>0: #If the hero blocks any damage at all
        hero.changeHP(round(blocked_hero)) #The blocked damage is added back (as the goblin attack function subtracted it)
#       print bob.getHP()
#       print hero.getHP()
    heroHPt, gobHPt = HP_check(win2,hero.getHP(),gob.getHP())
    time.sleep(2)
    taken.undraw()
    block.undraw()
    heroHPt.undraw()
    gobHPt.undraw()

def HP_check(win,hero_HP,gob_HP): #Displays the HP of both parties
    heroHPt=Text(Point(20,7),'Your HP is now at %d' % (hero_HP))
    heroHPt.setFace('papyrus')
    heroHPt.setSize(13)
    heroHPt.draw(win)
    gobHPt=Text(Point(20,27),"The Goblin's HP is now at %d" % (gob_HP))
    gobHPt.setFace('papyrus')
    gobHPt.setSize(13)
    gobHPt.draw(win)
    return heroHPt, gobHPt


def battle(win2,battack,bdefend,bob,hero,win,name): #Full battle sequence
    done=False
    while not done:
        p=win2.getMouse()
        if battack.clicked(p)==True: #If hero chooses to attack
            battack.undraw() #Undraws the buttons
            bdefend.undraw()
            hero_attack_whole(win2,hero,bob) #Attacks
            battack, bdefend = att_defbuttons(win2) #Draws buttons back on
            done=False
        if bdefend.clicked(p)==True: #If hero chooses to block
            battack.undraw()
            bdefend.undraw()
            hero_defend_whole(win2,hero,bob) #Defends
            battack, bdefend = att_defbuttons(win2)
            done=False
        if bob.getHP()<=0: #If and when the Goblin dies
            battack.undraw()
            bdefend.undraw()
            wint=Text(Point(20,29),"""You have defeated
                                the Goblin!""")
            wint.setSize(22)
            wint.setStyle('bold')
            wint.setFace('papyrus')
            wint.draw(win2)
            congrat=Text(Point(20,18),'Congrats, '+name+'!')
            congrat.setSize(22)
            congrat.setFace('papyrus')
            congrat.draw(win2)
            vict=Text(Point(20,7),"Demo Completed!")
            vict.setFace('papyrus')
            vict.setSize(22)
            vict.draw(win2)
            done=True
        
    p=win2.getMouse() #Ends game
    win2.close()
    win.close()

def main3(main_char):
    name=main_char.getName()
    hero=Character(main_char)
    print main_char
    print hero
    
    win=GraphWin('Game',600,600)
    win.setCoords(0.0,0.0,40.0,40.0)
    win.setBackground('lightseagreen')
    
    pic=Pixmap('sand.gif')
    img=Image(Point(20,20),pic)
    img.draw(win)

    makeSides(win)
    makeBorder(win)
    makeArrows(win)
    drawHero(win)
    bu,bd,bl,br = makeButtons(win)
    horiz=0
    vert=0
    movenum=0
    movement(win,bu,bd,bl,br,horiz,vert,movenum,img)
    win2=GraphWin('Battle',400,400)
    win2.setCoords(0,0,40,40)
    win2.setBackground('beige')
    bob=encounter(win2)
    battack, bdefend = att_defbuttons(win2)
    battle(win2,battack,bdefend,bob,hero,win,name)

