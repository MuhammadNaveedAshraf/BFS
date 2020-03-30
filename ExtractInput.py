from Test import *
file = open("file", 'r')
inputFile = []
states = []
actions = []
testCases = []

inputFile.append(file.readline())
noOfStates = int(inputFile[0].split()[0], 10)

noOfActions = int(inputFile[0].split()[1], 10)

noOfTestCases = int(inputFile[0].split()[2], 10)

noOfTestCases = int(inputFile[0].split()[2],10)
rows, cols = (noOfStates, noOfActions)
transitionTable =[[0 for i in range(cols)] for j in range(rows)]

for x in range(noOfStates):
    states.append(file.readline().rstrip('\n'))

for x in range(noOfActions):
    actions.append(file.readline().rstrip('\n'))

for x in range(noOfStates):
    rowData = file.readline()
    for y in range(noOfActions):
        transitionTable[x][y] = int(rowData.split()[y])

for x in range(noOfTestCases):
    line = file.readline()
    source = line.split(' (')[0]
    destination = line.split(') ')[1].rstrip('\n')
    # temp = {line.split(' (')[0], line.split(') ')[1].rstrip('\n')}
    testCases.append(Test(source,destination))
