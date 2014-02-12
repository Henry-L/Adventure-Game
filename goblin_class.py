import random

class Goblin:
    def __init__(self,hp,att,defe,ev):
        self.HP=hp
        self.AT=att
        self.DEF=defe
        self.EV=ev
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
        damage=(self.AT)*(random.uniform(1,2))
        return damage
    def defend(self):
        blocked=(self.DEF)*(random.uniform(.75,1.25))
        return blocked
