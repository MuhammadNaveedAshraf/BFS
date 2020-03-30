from ExtractPlan import ExtractPlan
from Node import *
from Test import *
from ExtractInput import *
class BFS:
    def __init__(self):
        for test in testCases:
            print("Plan for ", test.source, " to ", test.destination, ":")
            ExtractPlan(test.source, test.destination)


