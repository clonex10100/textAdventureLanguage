from items import *
from entities import *
#from area import *
import random
#function used to get player choice when in an area
def choice(options):
    pass

def encounter(player, enemy):
    out("You have encountered " + enemy.getName() + ".")
    flag = True
    while flag:
        out("What would you like to do?")
        out("Options: Attack, Inspect")
        i = inp().lower()
        if i == "attack":
            out("Which attack would you like to do?")
            attacks = player.getWeapon().getAttacks()

            for j in range(len(attacks)):
                out(str(j)+": " + attacks[j])

            while True:
                x = inp().lower()
                try:
                    x = int(x)
                except:
                    try:
                        x = attacks.index(x)
                    except:
                        x = -1
                if not x < 0:
                    if player.attack(enemy, x) < 0:
                        out("monster dead you win")
                        flag = False
                    break
                else:
                    out("Invalid attack")
            enemy.attack(player,random.randint(0,len(enemy.getWeapon().getAttacks())-1))

        elif i == "inspect":
            out(enemy.getDesc())
            #stuff

def out(x):
    print(x)

def inp():
    return input()
