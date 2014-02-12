import random

class Character:
    def __init__(self,person):
        if person.getClass()=='Warrior':
            self.HP=30
            self.AT=4
            self.DEF=3
            self.EV=1
        if person.getClass()=='Archer':
            self.HP=26
            self.AT=5
            self.DEF=2
            self.EV=2
        if person.getClass()=='Mage':
            self.HP=22
            self.AT=6
            self.DEF=1
            self.EV=2
    def __str__(self):
        mes='HP: '+str(self.HP)+', ATT: '+str(self.AT)+', DEF: '+str(self.DEF)+', EV: '+str(self.EV)
        return mes
    def getHP(self):
        return self.HP
    def getAT(self):
        return self.AT
    def getDEF(self):
        return self.DEF
    def getEV(self):
        return self.EV
    def changeHP(self,HPchange):
        self.HP=self.HP+HPchange
    def attack(self):
        damage=(self.AT)*(random.uniform(.75,2.2))
        return damage
    def defend(self):
        blocked=(self.DEF)*(random.uniform(.5,1.01))
        return blocked
