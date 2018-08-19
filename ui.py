from items import *
from entities import *
from area import *
#function used to get player choice when in an area
def choice(options):
    pass

def encounter(player, enemy):
    out("You have encountered " + enemy.getName() + ".")
    i = inp().lower()
    while True:
        out("What would you like to do?")
        out("Options: Attack, Inspect")
        if i == "attack":
            #stuff
        elif i:
            out(enemy.getDesc())
    

def out(x):
    print(x)

def inp():
    return input()
