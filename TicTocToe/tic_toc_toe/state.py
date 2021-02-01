class State:
    board:list[list[int]]
    evaluation:int
    isFinalState:bool

    def __init__(self , board):
        self.evaluation = 0
        self.board = board
        self.evaluation = None

        self.evaluate()
        self.checkIfFinal()
    
    def checkIfFinal(self):
        
        if self.evaluation != None:
            self.isFinalState = True
        else:
            self.isFinalState = False
    
    def changeBoard(self , cellNum:int , number:int):
        listNum = int(cellNum / 3)
        subListNum = int(cellNum % 3)

        if self.board[listNum][subListNum] != 0: return None

        newBoard = []
        for row in self.board:
            sublist = []
            for cell in row:
                sublist.append(cell)
            newBoard.append(sublist)

        newBoard[listNum][subListNum] = number
        newState = State(newBoard)

        return newState

    def evaluate(self):
            scoreSum = 0

            for row in self.board:
                for cell in row:
                    scoreSum += cell
                if scoreSum == 3:
                    self.evaluation = 1
                    return 
                if scoreSum == -3:
                    self.evaluation = -1
                    return
                scoreSum = 0

            scoreSum = 0
            for colNum in range(3):
                for rowNum in range(3):
                    scoreSum += self.board[rowNum][colNum]
                if scoreSum == 3:
                    self.evaluation = 1
                    return 
                if scoreSum == -3:
                    self.evaluation = -1
                    return
                scoreSum = 0

            if (self.board[0][0] == self.board[1][1] == self.board[2][2] == 1):
                self.evaluation = 1
            elif (self.board[0][2] == self.board[1][1] == self.board[2][0] == 1):
                self.evaluation = 1
            elif (self.board[0][2] == self.board[1][1] == self.board[2][0] == -1):
                self.evaluation = -1 
            elif (self.board[0][0] == self.board[1][1] == self.board[2][2] == -1):
                self.evaluation = -1
            
            for row in self.board:
                for cell in row:
                    if( cell == 0):
                        return
            self.evaluation = 0