from items import *
from utilities import parse
#from ui import *
import ui
#inventory class
class player():
    def __init__(self,name):
        self.name = name
        self.health=100
        self.armor = armorSet()
        self.inventory={}#map names to items
        self.weapon=None
    def getWeapon(self):
        return self.weapon

    def attack(self, enemy, attackIndex):
        attack = self.weapon.getAttack(self.weapon.getAttacks()[attackIndex])
        ui.inp()
        ui.out(self.name + " hits "+enemy.getName() + " with " + attack.getName())
        return enemy.hit(attack)
    def getName(self):
        return self.name
    def hit(self,attack):
        self.health -= self.armor.calcDamage(attack)
        if self.health <= 0:
            return -1
        else:
            return 0
class inventory():
    def __init__(self):
        pass

class enemy():
    def __init__(self,f):
        f = parse(f)
        self.name = f.get("name")
        self.desc = f.get("desc")
        self.health = int(f.get("health"))

        self.weapon = weapon(f.get("weapon"))
        self.armor = armorSet()

        for i in ["helm","chest","legs","boots"]:
            if f.get(i,-1) != -1:
                armor.set(armorPiece(f.get(i)))

        #How can drops be given to the player? It's a wierd thing for attack to handle
        #maps a tuple of the range to an item, eg (0,15):sword. 
        #usage: get a random number from 0 to 100, if 0 <= x <= 15 drop = sword
        self.drops={}
        for i in f.get("drops").split("\n"):
            i = i.split(" ")
            dropRange=i[1].split("-")
            self.drops[(dropRange[0],dropRange[1])] = createItem(i[0])

            

    def attack(self, enemy, attackIndex):
        attack = self.weapon.getAttack(self.weapon.getAttacks()[attackIndex])
        print(self.name + " hits "+enemy.getName() + " with " + attack.getName())
        return enemy.hit(attack)

    def hit(self,attack):
        self.health -= self.armor.calcDamage(attack)
        if self.health <= 0:
            return -1
        else:
            return 0

    def getName(self):
        return self.name
    def getDesc(self):
        return self.desc
    def getWeapon(self):
        return self.weapon
