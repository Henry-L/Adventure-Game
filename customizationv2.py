#This is the customization portion of the game, where the player can choose the
#type of hairstyle/clothing and weapon for their hero. This is done by having
#a stick figure model on which the various objects gets drawn on. The objects
#were made in a different program in which I drew the images point by point and
#then saved the coordinates on to text files. The text files are then read in and
#drawn onto the stick figure. As of now, the choices are not referenced later
#in the game but might be if more work is put into this in the future.

from graphics import *
from button_orig import *
import time

def SPerson(win): #Draws the stick person
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

def hair_buttons(win): #Buttons and text for changing hair
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

def object_move(win,ind,text_objects,object1,direction):
    #ind is the index which exists for all three changeable objects, is an int
    #text_objects is a list which contains the .txt files for the objects
    #object1 is the name of the object that is being changed, is a string
    #direction is either up or down, represents moving either up or down the list of text_objects
    if direction=='up':
#        print ind
        if -1>ind or ind >=(len(text_objects)-1): #Testing whether or not ind is out of list's range
            return ind, object1
        else:
            ind=ind+1 #Moves up the list
            inputf=open(text_objects[ind],'r') #Opens the text file corresponding to the index
            data=inputf.readlines() #Reads in the numbers
            objectX=data[0].split() #Creates a list of Xs
            objectY=data[2].split() #Creates a list of Ys

            pList=[] #List of points
            for i in range(len(objectX)):
                    pList.append(Point(float(objectX[i]),float(objectY[i]))) #Creates points from Xs and Ys and appends them to list
            if object1=='hair':
                object1=Polygon(pList)
                object1.setFill('black') #If its hair, draw it and make it black
            elif object1=='shirt':
                object1=Polygon(pList)
                object1.setFill('brown') #If its a shirt, draw it and make it brown
            elif object1=='weapon':
                object1=Polygon(pList)
                object1.setFill('gray') #If its a weapon, draw it and make it gray
            object1.draw(win)
#        print ind
        return ind, object1
    else:
#        print ind
        if 1>ind:
            return ind, object1
        else:
            ind=ind-1
            inputf=open(text_objects[ind],'r')
            data=inputf.readlines()
            objectX=data[0].split()
            objectY=data[2].split()

            pList=[]
            for i in range(len(objectX)):
                    pList.append(Point(float(objectX[i]),float(objectY[i])))
            if object1=='hair':
                object1=Polygon(pList)
                object1.setFill('black')
            elif object1=='shirt':
                object1=Polygon(pList)
                object1.setFill('brown')
            elif object1=='weapon':
                object1=Polygon(pList)
                object1.setFill('gray')
            object1.draw(win)
#        print ind
        return ind, object1






def main2():
    win=GraphWin('customization',500,700)
    win.setBackground('beige')
    win.setCoords(0.0,0.0,50.0,70.0)
    SPerson(win)
    shirtup,shirtdown = shirt_buttons(win)
    hairup,hairdown = hair_buttons(win)
    weaponup,weapondown = weapon_buttons(win)
    bquit=Button(win,Point(24,5),8,4.5,'DONE')
    bquit.setSize(16)
    hairs=['lhair.txt','spikey.txt','h-hair.txt','mohawk.txt','bowl.txt','girl2.txt']
    shirts=['vneck.txt','warrior.txt','vest.txt','tshirt.txt','ragged.txt','sack.txt']
    weapons=['stick.txt','sword.txt','bow.txt','spike_thing.txt','broom.txt']
    ind_hair=-1
    ind_shirt=-1
    ind_weapon=-1
    done=False
    while not done:
        p=win.getMouse()
        if hairup.clicked(p)==True:
            if ind_hair>=0:
                try:
                    hair.undraw()
                except AttributeError: #In case list index is at a point where the function won't draw in hair and the function tries to undraw a string
                    done=False
            try:
                ind_hair,hair = object_move(win,ind_hair,hairs,'hair','up')
                done=False
            except UnboundLocalError: #When list index still ends up out of range
                done=False
        elif hairdown.clicked(p)==True:
            if ind_hair>=0:
                try:
                    hair.undraw()
                except AttributeError:
                    done=False
            try:
                ind_hair,hair = object_move(win,ind_hair,hairs,'hair','down')
                done=False
            except UnboundLocalError:
                done=False
        if shirtup.clicked(p)==True:
            if ind_shirt>=0:
                try:
                    shirt.undraw()
                except AttributeError:
                    done=False
            try:
                ind_shirt,shirt = object_move(win,ind_shirt,shirts,'shirt','up')
                done=False
            except UnboundLocalError:
                done=False
        elif shirtdown.clicked(p)==True:
            if ind_shirt>=0:
                try:
                    shirt.undraw()
                except AttributeError:
                    done=False
            try:
                ind_shirt,shirt = object_move(win,ind_shirt,shirts,'shirt','down')
                done=False
            except UnboundLocalError:
                done=False

        if weaponup.clicked(p)==True:
            if ind_weapon>=0:
                try:
                    weapon.undraw()
                except AttributeError:
                    done=False
            try:
                ind_weapon,weapon = object_move(win,ind_weapon,weapons,'weapon','up')
                done=False
            except UnboundLocalError:
                done=False
        elif weapondown.clicked(p)==True:
            if ind_weapon>=0:
                try:
                    weapon.undraw()
                except AttributeError:
                    done=False
            try:
                ind_weapon,weapon = object_move(win,ind_weapon,weapons,'weapon','down')
                done=False
            except UnboundLocalError:
                done=False
        elif bquit.clicked(p)==True:
            bquit.undraw()
            mes=Text(Point(25,4),'Lookin good')
            mes.setFace('papyrus')
            mes.setSize(18)
            mes.draw(win)
            time.sleep(2)
            mes.undraw()
            mes=Text(Point(25,4),'Off to the desert!')
            mes.setFace('papyrus')
            mes.setSize(18)
            mes.draw(win)
            time.sleep(3.5)
            done=True

    win.close()

        
