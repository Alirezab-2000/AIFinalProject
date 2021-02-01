from typing import Any, Tuple
from MazeSolver.node import Node

class MazeWorld:
    rowsNumber:int
    columnsNumber:int
    allNodes:list[Node] = []
    size:int

    def __init__(self , x , y):
        self.rowsNumber = x
        self.columnsNumber = y
        self.size = x * y

    def gnerateMaze(self):
        mazeRoot = Node() 
        mazeRoot.name = "1"
        mazeRoot.row = 1
        mazeRoot.column = 1
        
        self.allNodes.append(mazeRoot)
        self.conectNodes(mazeRoot)

        # horizontal walls
        self.setMultipleWall([
            ("3" , "4"),("5" , "6"),("8" , "9"),
            ("12" , "13"),("13" , "14"),("15" , "16"),
            ("16" , "17"),("18" , "19"),("19" , "20"),
            ("21" , "22"),("22" , "23"),("23" , "24"),
            ("24" , "25"),("27" , "28"),("29" , "30"),
            ("31" , "32"),("32" , "33"),("34" , "35"),
            ("41" , "42"),("45" , "46"),("48" , "49"),
            ("52" , "53"),("54" , "55"),("57" , "58"),
            ("58" , "59"),("61" , "62"),("65" , "66"),
            ("67" , "68"),("71" , "72"),("73" , "74"),
            ("74" , "75"),("75" , "76"),("78" , "79"),
            ("79" , "80"),("81" , "82"),("82" , "83"),
            ("83" , "84"),("88" , "89"),("89" , "90"),
            ("93" , "94"),("98" , "99")
            ])
    
        # Vertical walls
        self.setMultipleWall([
            ("2" , "12"),("4" , "14"),("7" , "17"),
            ("15" , "25"),("16" , "26"),("18" , "28"),
            ("26" , "36"),("27" , "37"),("28" , "38"),
            ("29" , "39"),("33" , "43"),("34" , "44"),
            ("36" , "46"),("37" , "47"),("38" , "48"),
            ("39" , "49"),("42" , "52"),("44" , "54"),
            ("45" , "55"),("50" , "60"),("53" , "63"),
            ("56" , "66"),("59" , "69"),("62" , "72"),
            ("63" , "73"),("67" , "77"),("68" , "78"),
            ("70" , "80"),("75" , "85"),("76" , "86"),
            ("77" , "87"),("78" , "88"),("82" , "92"),
            ("84" , "94"),("85" , "95"),("86" , "96"),
            ("87" , "97")
            
        ]) 
        
        return mazeRoot

    def conectNodes(self , root : Node):

        myNode = root
        for x in range(1 , self.columnsNumber):
            rightNode = Node()
            rightNode.column = myNode.column + 1
            rightNode.row = myNode.row
            rightNode.name = str(int(myNode.name) + 1)
            myNode.right = rightNode
            self.allNodes.append(rightNode)
            rightNode.left = myNode
            myNode = myNode.right
        
        myNode = root
        for x in range(1 , self.rowsNumber):
            firstBottomNode = Node()
            firstBottomNode.column = myNode.column
            firstBottomNode.row = myNode.row + 1
            firstBottomNode.name = str(int(myNode.name) + self.columnsNumber)
            myNode.bottom = firstBottomNode
            firstBottomNode.top = myNode
            self.allNodes.append(firstBottomNode)
            myNode = myNode.right

            while myNode != None:
                bottomNode = Node()
                bottomNode.column = myNode.column
                bottomNode.row = myNode.row + 1
                bottomNode.name = str(int(myNode.name) + self.columnsNumber)
                myNode.bottom = bottomNode
                bottomNode.top = myNode
                bottomNode.left = myNode.left.bottom
                myNode.left.bottom.right = bottomNode
                self.allNodes.append(bottomNode)
                myNode = myNode.right
            
            myNode = firstBottomNode

    def searchNode(self , nodeName:str):
        if self.allNodes == []:
            self.gnerateMaze()
        
        for node in self.allNodes:
            if(node.name == nodeName):
                return node
        
        return -1

    def setOrUnsetWall(self , firstNodeName:str , secondNodeName:str):
        firstNodeNameNum = int(firstNodeName)
        secondNodeNameNum = int(secondNodeName)

        if abs(firstNodeNameNum - secondNodeNameNum) != 1 and abs(firstNodeNameNum - secondNodeNameNum) != self.columnsNumber:
            raise Exception("invalid input for change wall state")
        
        firstNode:Node = None
        secondNode:Node = None

        for node in self.allNodes:
            if(node.name == firstNodeName):
                firstNode = node
            elif(node.name == secondNodeName):
                secondNode = node
            if firstNode is not None and secondNode is not None:
                break
  
        if((firstNodeNameNum - secondNodeNameNum) == 1):
            if(firstNode.leftWall and secondNode.rightWall):
                firstNode.leftWall = False
                secondNode.rightWall = False
            else:    
                firstNode.leftWall = True
                secondNode.rightWall = True

        elif((secondNodeNameNum - firstNodeNameNum) == 1):
            if(firstNode.leftWall and secondNode.rightWall):
                secondNode.leftWall = False
                firstNode.rightWall = False
            else:
                secondNode.leftWall = True
                firstNode.rightWall = True

        elif ((secondNodeNameNum - firstNodeNameNum) == self.columnsNumber):
             if(firstNode.bottomWall and secondNode.topWall):
                 secondNode.topWall = False
                 firstNode.bottomWall = False
             else:    
                secondNode.topWall = True
                firstNode.bottomWall = True
        
        else:
             if(firstNode.topWall and secondNode.bottomWall):
                 firstNode.topWall = False
                 secondNode.bottomWall = False
             else:    
                firstNode.topWall = True
                secondNode.bottomWall = True

    def setMultipleWall(self , nodes :list[Tuple[str , str]]):
        for x in nodes:
            self.setOrUnsetWall(x[0] , x[1])

    # drawing method -----------------

    def drawTheMaze(self , root:Node ,goalNodeNum:str , startNodeNum:str):
        mySize = self.size
        rowSize = 11 * self.columnsNumber
        colSize = 2 * self.rowsNumber + 1

        print (" ═"+rowSize * "═")

        firstColNode = root
        while firstColNode != None:
            rowItr = firstColNode
            rowText = "║"
            bottomText = "║"
            while rowItr != None:
                rowText += "{:<10}".format(self.getText(rowItr.name , goalNodeNum , startNodeNum))

                if rowItr.rightWall :
                    rowText += "║"
                else:
                    rowText += " "
                
                if rowItr.bottomWall:
                    bottomText += "═══════════"
                else:
                    bottomText += "           "
                
                rowItr = rowItr.right
            print(rowText + "║")
            if firstColNode.bottom == None:
                print(" ═" + rowSize * "═")
            else:
                print(bottomText + "║")
            firstColNode = firstColNode.bottom

    def getText(self , number:str,goalNodeNum:str , startNodeNum:str):
        text =""
        if len(number) == 1:
            text =  "     "+number
        elif len(number) == 2:
            text =  "    "+number
        else:
            text =  "   "+number
        
        if(number == goalNodeNum):
            text += " (g)"
        elif (number == startNodeNum):
            text += " (s)"
        return text