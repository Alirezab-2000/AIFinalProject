from MazeSolver.node import Node


class State:
    node: Node
    stateFather: "State"
    pathCost: int
    manhatanDistance: int

    def __init__(self):
        self.pathCost = 0
        self.manhatanDistance = 0
        self.stateFather = None

    def __lt__(self, state : "State"):
        return (
            self.pathCost + self.manhatanDistance
            < state.pathCost + state.manhatanDistance
        )
