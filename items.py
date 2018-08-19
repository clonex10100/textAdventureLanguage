from utilities import parse

def createItem(f):
    a = {"item":item,"armorPiece":armorPiece,"weapon":weapon}
    b = parse(f)
    return a[b.get("class")](f)

class item():
    def __init__(self,f):
        f = parse(f)
        protection = f.get("protection")
        self.name = f.get("name")
        self.value = f.get("value")

    def getDesc(self):
        return self.desc

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

#a single piece of armor
class armorPiece(item):
    def __init__(self,f):
        super().__init__(f)

        f = parse(f)

        self.protection={}
        for i in f.get("protection").split("\n"):
            i = i.split(" ")
            self.protection[i[0]] = int(i[1])

        self.type = f.get("type")
    def getProtection(self,dType):
        return self.protection.get(dType)
    def getType(self):
        return self.type

class weapon(item):
    def __init__(self,f):
        super().__init__(f)

        f = parse(f)

        self.attacks={}
        for i in f.get("attacks").split("\n"):
            att = attack(i)
            self.attacks[att.getName()] = att

    def getAttacks(self):
        return list(self.attacks.keys())
    def getAttack(self,attack):
        return self.attacks.get(attack)

class attack(item):
    def __init__(self,f):
        super().__init__(f)

        f = parse(f)

        self.type = f.get("type")
        self.damage = int(f.get("damage"))

    def getType(self):
        return self.type
    def getDamage(self):
        return self.damage

#a set of armor worn by an entidy
class armorSet():
    def __init__(self):
        self.armor={"helm":None,"chest":None,"leg":None,"boot":None}
        self.protection=0

    def getArmor(val):
        return self.get(val,-1)

    def set(self,armor):
        try:
            self.armor[armor.getType()] = armor
            return 0
        except:
            return -1

    def calcDamage(self,attack):
        return int(attack.getDamage() * (0.01*(100 - sum([self.armor.get(i).getProtection(attack.getType) if self.armor.get(i) != None else 0 for i in self.armor.keys()]))))


