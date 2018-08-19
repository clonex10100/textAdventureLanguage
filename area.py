from items import *
from entities import *
class varHandler():
    #Designed to offer consistant flags accessible by area/dialogue nodes
    def __init__(self):
        self.vars={}
    def setVar(self,var,val):
        self.vars[var]=val
    def getVar(self,var):
        return self.vars.get(var ,False)
    def getVars(self):
        return self.vars.keys()
    def mod(self,var,amount):
        try:
            self.vars[var] += amount
            return 0
        except:
            return -1
class area():
    ifKeywords=["not","match","input","have","<",">"]
    varsH = varHandler()
    player = player("Noah")

    def __init__(self,areaFile):
            self.file = open(areaFile,"r")

    def eval(self,statement):
        if statement[0] in self.ifKeywords:
            if statement[0] == "not":
                return not area.varsH.getVar(statement[1])
        else:
            return area.varsH.getVar(statement[0])

    def ifHandler(self,line):
        statement=[]
        for i in line:
            if i == "or":
                result = self.eval(statement)
                if result:
                    return True
                else:
                    return self.ifHandler(line[len(statement)+1:])
            elif i == "and":
                result = self.eval(statement)
                if result:
                    return self.ifHandler(line[len(statement)+1:])
                else:
                    return False 
            statement.append(i)

    def run(self):
            #Local variables
            inPrint = False
            skipIf = False
            for line in self.file:
                line=line[:-1]
                #first, check if in a block. If so, do stuff
                if inPrint:
                    if line == "~endprint~":
                        inPrint = False
                    else:
                        print(line)

                elif line == "endif":
                    skipIf = False

                #if if statement check failed, skip statements untill end
                if not skipIf:

                    #check for single work commands
                    if line == "~print~":
                        inPrint = True
    
                    #now for commands with multiple words. Split the line to help parse
                    line = line.split(" ")
                    if line[0] == "if":
                        skipIf = not self.ifHandler(line[1:])
                    elif line[0] == "goto":
                        self.file.close()
                        return line[1]
                    elif line[0] == "set":
                        area.varsH.setVar(line[1],line[2])
            self.file.close()
            return 0


thePlayer = player("Christopher")
a = area("areaTest")
while True:
    nex=a.run()
    if nex != 0:
        a=area(nex)
    else:
        print("Hit end")
        break
