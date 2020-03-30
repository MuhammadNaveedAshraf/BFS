from BFS import *
from showPlan import showPlan
from Node import *
from ExtractInput import *


def ExtractPlan(source,destination):
    start = Node(stateNumber(source), None)
    desti = Node(stateNumber(destination), None)
    currentState = start
    # children = []
    frontier = []
    goalFound = False
    exploredSet = []
    if source == destination:
        print("Do Nothing")
    else:
        frontier.append(currentState)
        while frontier.__len__() != 0 and goalFound != True:

            currentState=frontier.pop(0)
            temp = searchNode(exploredSet, currentState)
            if not temp:
                exploredSet.append(currentState)
            children = getchildren(currentState.number)
            while children.__len__() != 0:
                child = children.pop(0)
                if child.number == desti.number:
                    goalFound = True
                    currentState = child
                else:
                    temp = searchNode(exploredSet, child)
                    if not temp:
                        frontier.append(child)

        if goalFound == False:
            print("Goal Not Found")
        else:
            showPlan(start,currentState,exploredSet)




def stateNumber(state):
    for i in range(0, states.__sizeof__()):
        if states[i] == state:
            return i


def getchildren(parent):
    children = []
    for action in range(0, noOfActions):
        if parent != transitionTable[parent][action]:
            children.append(Node(transitionTable[parent][action], parent))
    return children

def searchNode(exploredSet, element):
    for node in exploredSet:
        if node.number == element.number:
            return True
    return False