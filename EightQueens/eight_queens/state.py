from typing import Tuple


class State:
    chess: list[list[int]] 
    evaluation:int
    queensPosition:list[Tuple[int , int]] 

    def __init__(self , theChess: list[list[int]]):
        self.chess = theChess
        self.evaluation = 0
        self.queensPosition = []

        self.getEvaluation()
        self.getQueensPosition()

    def getEvaluation(self):
        columnNumber = 0
        while columnNumber < 8:
            for rowNumber in range(8):
                if(self.chess[rowNumber][columnNumber] == 1):
                    col = columnNumber + 1
                    row = rowNumber - 1

                    while row > -1 and col < 8:
                        if self.chess[row][col] == 1:
                            self.evaluation += 1
                        row -= 1
                        col += 1
                
                    row = rowNumber + 1
                    col = columnNumber + 1

                    while row < 8  and col < 8:
                        if self.chess[row][col] == 1:
                            self.evaluation += 1
                        row += 1
                        col += 1
                
                    col = columnNumber + 1
                    row = rowNumber

                    while col < 8:
                        if self.chess[row][col] == 1:
                            self.evaluation += 1
                        col += 1
            columnNumber += 1
            rowNumber = 0
    
    def moveQueen(self , numberOfQueen:int  , destinationPosition:int):
        if numberOfQueen < 0 or numberOfQueen > 7 or destinationPosition < 0 or destinationPosition > 7:
            raise Exception("invalid movment")
        
        newChess = self.deepCopy()
        for rowNum in range(8):
            if(newChess[rowNum][numberOfQueen] == 1):
                newChess[rowNum][numberOfQueen] = 0
                newChess[destinationPosition][numberOfQueen] = 1
                break
        
        newState = State(newChess)

        return newState
    
    def getQueensPosition(self):
        for x in range(8):
            for y in range(8):
                if self.chess[y][x] == 1:
                    self.queensPosition.append((x , y))

    def deepCopy(self):
        newChess = []

        for x in self.chess:
            subChess = []
            for y in x:
                subChess.append(y)
            newChess.append(subChess)
        return newChess

    def drawState(self):
        
       print("║"+ 8 * "═════║")
       for x in self.chess:
           text = "║"
           for y in x:
               text += "{:<5}".format("  "+str("*" if y==1 else "")) + "║"
           print(text)

           print("║"+ 8 * "═════║")