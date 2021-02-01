from MazeSolver.state import State
from MazeSolver.node import Node
from typing import Tuple

def getSuccessor(state:State):
    node = state.node
    children:list[Node] = [ 
      None if node.topWall else node.top 
    , None if node.rightWall else node.right 
    , None if node.leftWall else node.left 
    , None if node.bottomWall else node.bottom
    ]
    
    successor : list[State] = []
    
    for child in children:
        if(child == None or child == node.father):
            continue
        
        childState = State()
        childState.node = child
        childState.stateFather = state
        childState.pathCost = state.pathCost + 1
        successor.append(childState)
    
    return successor
