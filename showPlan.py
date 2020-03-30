from ExtractInput import *
from ExtractPlan import *
#from ExtractPlan import searchNode


def showPlan(source, destination, exploredSet):
    actionList = []
    currentstate = destination
    while currentstate != source:
        for i in range(0, noOfActions):

            if currentstate.number == transitionTable[currentstate.parent][i]:
                actionList.append(actions[i])
                currentstate=getParent(exploredSet,currentstate)

        #while actionList.__len__()!=0:
    print (actionList)


def getParent(exploredSet,child):
    for parent in exploredSet:
        if child.parent == parent.number:
            return parent


