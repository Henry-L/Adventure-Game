
class Person:
    def __init__(self,name,classi):
        self.name=name
        self.classi=classi
    def __str__(self):
        mes='Name: '+self.name+', Class: '+self.classi
        return mes
    def getName(self):
        return self.name
    def getClass(self):
        return self.classi
