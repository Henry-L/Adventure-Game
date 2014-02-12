# button.py
#    A simple Button widget.

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.center=center
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        self.p1 = Point(self.xmin, self.ymin)
        self.p2 = Point(self.xmax, self.ymax)
#        self.rect = Rectangle(p1,p2)
#        self.rect.setFill('lightgray')
#        self.rect.draw(win)
#        self.label = Text(center, label)
#        self.label.draw(win)
        self.activate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
#        self.label.setFill('black')
#        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def drawButton(self,label,win):
        self.rect = Rectangle(self.p1,self.p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(self.center, label)
        self.label.draw(win)

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()
        self.active=False

    def setSize(self,num):
        self.label.setSize(num)

