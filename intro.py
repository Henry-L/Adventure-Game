#This is the intro section of the game. This sets the mood with the special font
#and colors. Also, it gets the basic information from the player and shows the
#quest instructions. Nothing too special, just a lot of text.

from graphics import *
from button2 import *
from character_class import *
from person_class import *
import time, string


def intro(win): #First set of intro texts, get the name of player
    hello=Text(Point(25,29),'Hello, Adventurer!')
    intro=Text(Point(25,23),'I hope you are ready for your quest')
    namet=Text(Point(25,17), 'Now.. what was your name again?')
    texts=[hello,intro,namet]
    for i in texts:
        i.setFace('papyrus')
        i.setSize(19)
    p=win.getMouse()
    hello.setStyle('bold')
    hello.draw(win)
    time.sleep(1.5)
    intro.draw(win)
    time.sleep(2.25)
    namet.draw(win)
    time.sleep(2.25)
    namebox=Entry(Point(25,10),10)
    namebox.setFace('papyrus')
    namebox.draw(win)
    b1=Button(win,Point(25,6),7,3,'Tell him')
    done=False
    while not done:
        p=win.getMouse()
        if b1.clicked(p)==True:
            name=namebox.getText()
            done=True
        else:
            done=False
    for i in texts:
        i.undraw()
    b1.undraw()
    namebox.undraw()
    name=name.capitalize()
    return name

def intro2(win,name): #Second set of intro text, references name and gets class choice
    hello2=Text(Point(25,28),'Ahh, thats right! How could I forget!')
    welc=Text(Point(25,21),name+', the best looking one of them all!')
    classt=Text(Point(25,14),'Remind me.. what class are you?')
    texts=[hello2,welc,classt]
    for i in texts:
        i.setFace('papyrus')
        i.setSize(20)
    hello2.draw(win)
    time.sleep(2)
    welc.draw(win)
    time.sleep(2)
    classt.draw(win)
    time.sleep(1)
    bwarrior=Button(win,Point(13,6),8,5,'Warrior')
    barcher=Button(win,Point(25,6),8,5,'Archer')
    bmage=Button(win,Point(37,6),8,5,'Mage')
    done=False
    while not done:
        p=win.getMouse()
        if bwarrior.clicked(p)==True:
            classi='Warrior'
            done=True
        elif barcher.clicked(p)==True:
            classi='Archer'
            done=True
        elif bmage.clicked(p)==True:
            classi='Mage'
            done=True
        else:
            done=False
    for i in texts:
        i.undraw()
    bwarrior.undraw()
    barcher.undraw()
    bmage.undraw()

    return classi

def transition(classi,win): #Gives quest instructions and transitions player to armory
    mes=Text(Point(25,28),classi+'! Fantastic class.')
    move=Text(Point(25,21),'Now head to the armory and gear up.')
    instruc=Text(Point(25,17),"""Your quest is simple, head to
the desert and defeat that pesky goblin
that has been causing us problems.""")
    texts=[mes,move,instruc]
    for i in texts:
        i.setFace('papyrus')
        i.setSize(20)
    mes.draw(win)
    time.sleep(1.5)
    instruc.setSize(18)
    instruc.draw(win)
    time.sleep(6)
    instruc.undraw()
    move.draw(win)
    time.sleep(1.5)
    bmove=Button(win,Point(25,9),16,8,'Go to Armory')
    bmove.setSize(14)
    done=False
    while not done:
        p=win.getMouse()
        if bmove.clicked(p)==True:
            done=True
        else:
            done=False
    for i in texts:
        i.undraw()
    bmove.undraw()
    

def main1():
    win=GraphWin("Adventure Start",500,350)
    win.setBackground('beige')
    win.setCoords(0,0,50,35)
    name=intro(win)
    classi=intro2(win,name)
    main_char=Person(name,classi)
    transition(classi,win)
    win.close()
    return main_char

