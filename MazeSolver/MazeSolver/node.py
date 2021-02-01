class Node:
    row:int
    column:int
    name:str

    father : 'Node'
    left : 'Node'
    top : 'Node'
    right : 'Node'
    bottom : 'Node'

    topWall:bool
    rightWall:bool
    leftWall:bool
    bottomWall:bool

    def __init__(self):
        self.right = None
        self.left = None
        self.bottom = None
        self.top = None
        self.father = None
        self.row = 0
        self.column = 0
        self.name = "0"
        self.rightWall = False
        self.bottomWall = False
        self.topWall = False
        self.leftWall = False


