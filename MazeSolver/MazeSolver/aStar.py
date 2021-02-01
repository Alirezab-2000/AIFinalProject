from MazeSolver.state import State
from MazeSolver.getSuccessor import getSuccessor
from MazeSolver.mazeWorld import MazeWorld
from MazeSolver.priorityQueue import PriorityQueue
from MazeSolver.getManhatanDistance import getManhatanDistance
from MazeSolver.getSuccessor import getSuccessor
from MazeSolver.node import Node
from typing import Tuple

def aStarAlgoritm(startNodeName , mazeWorld:MazeWorld , goalNodeName):
    startNode = mazeWorld.searchNode(startNodeName)
    goalNode = mazeWorld.searchNode(goalNodeName)
    aStarQueue = PriorityQueue()
    path:list[str] = []

    if startNode == goalNode :
        path = "the start state is the goal!"
        return path

    startNodeManhatanDistance = getManhatanDistance(startNode , goalNode)
    startState = State()
    startState.node = startNode
    startState.manhatanDistance = startNodeManhatanDistance
    aStarQueue.enqueue(startState)
    
    pathText2 = ""
    while aStarQueue.size() != 0:
        state = aStarQueue.dequeue()

        if state.node == goalNode:
            return getPath(state)

        # pathText2 += state.node.name
        successors:list[State] = getSuccessor(state)

        for childState in successors:
            nodeManhatanDistance = getManhatanDistance(childState.node , goalNode)
            childState.manhatanDistance = nodeManhatanDistance
            aStarQueue.enqueue(childState)

    return "this maze has no answer..."

def getPath(state : State):
    path:list[str] = []

    while state != None:
        path.append(state.node.name)
        state = state.stateFather
    path.reverse()
    
    pathText = ""
    for index in range(len(path)):
        if index == 0:
            pathText += path[0]
            continue

        pathText += " ---> "+ path[index]

    return pathText