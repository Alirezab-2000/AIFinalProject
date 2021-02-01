from MazeSolver.node import Node

def getManhatanDistance(node:Node , goalNode:Node):
    return abs(goalNode.column - node.column) + abs(goalNode.row - node.row)