from graphics import *
from button_orig import *

    
win=GraphWin('customization',500,700)
win.setBackground('beige')
win.setCoords(0.0,0.0,50.0,70.0)


def Person(win):
    head=Circle(Point(25,59),6)
    body=Line(Point(25,53),Point(25,34))
    arml=Line(Point(25,48),Point(13,48))
    armr=Line(Point(25,48),Point(37,45))
    legl=Line(Point(25,34),Point(17,26))
    legr=Line(Point(25,34),Point(33,26))
    head.draw(win)
    body.draw(win)
    arml.draw(win)
    armr.draw(win)
    legl.draw(win)
    legr.draw(win)

def hair_buttons(win):
    hairup=Button(win,Point(18,17),3,3,'')
    hairt=Text(Point(13,17),'HAIR')
    hairt.setSize(15)
    hairt.draw(win)
    hairdown=Button(win,Point(8,17),3,3,'')
    return hairup, hairdown

def shirt_buttons(win):
    shirtup=Button(win,Point(42,17),3,3,'')
    shirtt=Text(Point(36,17),'SHIRT')
    shirtt.setSize(15)
    shirtt.draw(win)
    shirtdown=Button(win,Point(30,17),3,3,'')
    return shirtup, shirtdown

def weapon_buttons(win):
    weaponup=Button(win,Point(31,11),3,3,'')
    weapont=Text(Point(24,11),'WEAPON')
    weapont.setSize(15)
    weapont.draw(win)
    weapondown=Button(win,Point(17,11),3,3,'')
    return weaponup, weapondown

def hair_up(win,ind_hair,hairs):
    print ind_hair
    print -1>ind_hair
    print ind_hair>=(len(hairs))
    if -1>ind_hair or ind_hair >=(len(hairs)-1):
        done=False
    else:
        ind_hair=ind_hair+1
        inputf=open(hairs[ind_hair],'r')
        data=inputf.readlines()
        hairX=data[0].split()
        hairY=data[2].split()

        pList=[]
        for i in range(len(hairX)):
                pList.append(Point(float(hairX[i]),float(hairY[i])))
        hair=Polygon(pList)
        hair.setFill('black')
        hair.draw(win)
        print ind_hair
        done=False
    return ind_hair, hair

hairs=['lhair.txt','spikey.txt','h-hair.txt','mohawk.txt']
shirts=['vneck.txt','warrior.txt','vest.txt','tshirt.txt']
weapons=['stick.txt','sword.txt','bow.txt','spike_thing.txt']
ind_hair=-1
ind_shirt=-1
ind_weapon=-1

Person(win)
shirtup,shirtdown = shirt_buttons(win)
hairup,hairdown = hair_buttons(win)
weaponup,weapondown = weapon_buttons(win)

done=False
while not done:
    p=win.getMouse()
    if hairup.clicked(p)==True:
        if ind_hair>=0:
            hair.undraw()
        try:
            ind_hair, hair = hair_up(win,ind_hair,hairs)
        except UnboundLocalError:
            done=False
    elif hairdown.clicked(p)==True:
        print ind_hair
        print 0>ind_hair
        print ind_hair>=(len(hairs))
        if 1>ind_hair or ind_hair>=(len(hairs)):
            done=False
        else:
            if ind_hair>=0:
                hair.undraw()
            ind_hair=ind_hair-1 #There is an issue with not being able to display last hairstyle
            inputf=open(hairs[ind_hair],'r')
            data=inputf.readlines()
            hairX=data[0].split()
            hairY=data[2].split()

            pList=[]
            for i in range(len(hairX)):
                pList.append(Point(float(hairX[i]),float(hairY[i])))
            hair=Polygon(pList)
            hair.setFill('black')
            hair.draw(win)
            print ind_hair
            done=False
    if shirtup.clicked(p)==True:
        if ind_shirt>=0:
            shirt.undraw()
        print ind_shirt
        print -1>ind_shirt
        print ind_shirt>=(len(shirts))
        if -1>ind_shirt or ind_shirt>=(len(shirts)-1):
            done=False
        else:
            ind_shirt=ind_shirt+1
            inputf=open(shirts[ind_shirt],'r')
            data=inputf.readlines()
            shirtX=data[0].split()
            shirtY=data[2].split()

            pList=[]
            for i in range(len(shirtX)):
                pList.append(Point(float(shirtX[i]),float(shirtY[i])))
            shirt=Polygon(pList)
            shirt.setFill('brown')
            shirt.draw(win)
            print ind_shirt
            done=False
    elif shirtdown.clicked(p)==True:
        print ind_shirt
        print 0>ind_shirt
        print ind_shirt>=(len(shirts))
        if 1>ind_shirt or ind_shirt>=(len(shirts)):
            done=False
        else:
            if ind_shirt>=0:
                shirt.undraw()
            ind_shirt=ind_shirt-1 #There is an issue with not being able to display last shirtstyle
            inputf=open(shirts[ind_shirt],'r')
            data=inputf.readlines()
            shirtX=data[0].split()
            shirtY=data[2].split()

            pList=[]
            for i in range(len(shirtX)):
                pList.append(Point(float(shirtX[i]),float(shirtY[i])))
            shirt=Polygon(pList)
            shirt.setFill('brown')
            shirt.draw(win)
            print ind_shirt
            done=False

    if weaponup.clicked(p)==True:
        if ind_weapon>=0:
            weapon.undraw()
        print ind_weapon
        print -1>ind_weapon
        print ind_weapon>=(len(weapons))
        if -1>ind_weapon or ind_weapon>=(len(weapons)-1):
            done=False
        else:
            ind_weapon=ind_weapon+1
            inputf=open(weapons[ind_weapon],'r')
            data=inputf.readlines()
            weaponX=data[0].split()
            weaponY=data[2].split()

            pList=[]
            for i in range(len(weaponX)):
                pList.append(Point(float(weaponX[i]),float(weaponY[i])))
            weapon=Polygon(pList)
            weapon.setFill('gray')
            weapon.draw(win)
            print ind_weapon
            done=False
    elif weapondown.clicked(p)==True:
        print ind_weapon
        print 0>ind_weapon
        print ind_weapon>=(len(weapons))
        if 1>ind_weapon or ind_weapon>=(len(weapons)):
            done=False
        else:
            if ind_weapon>=0:
                weapon.undraw()
            ind_weapon=ind_weapon-1 #There is an issue with not being able to display last weaponstyle
            inputf=open(weapons[ind_weapon],'r')
            data=inputf.readlines()
            weaponX=data[0].split()
            weaponY=data[2].split()

            pList=[]
            for i in range(len(weaponX)):
                pList.append(Point(float(weaponX[i]),float(weaponY[i])))
            weapon=Polygon(pList)
            weapon.setFill('gray')
            weapon.draw(win)
            print ind_weapon
            done=False
    




        
