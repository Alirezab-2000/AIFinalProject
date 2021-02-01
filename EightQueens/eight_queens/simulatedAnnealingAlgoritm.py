from eight_queens.state import State
import random
import math


class SimulatedAnnealing:
    currentState:State
    temp:float = 10

    def __inti__(self):
        self.currentState = None
        self.randomStart()
    
    def randomStart(self):
        chessBoard = [[0 for i in range(8)] for j in range(8)]

        for x in range(8):
            col = random.randint(0 , 7)
            chessBoard[col][x] = 1
        
        self.currentState = State(chessBoard)
        self.currentState.drawState()


    def saAlgoritm(self):
        
        while self.temp > 0:
            if (self.currentState.evaluation == 0):
                print("answer found")
                break
            
            newState  = self.randomState()

            if self.isNewStateValid(newState) :
                self.currentState = newState
            self.schedule()    
            

        if self.temp <= 0 : print("the T param be cold")
        self.currentState.drawState()

    def schedule(self):
        self.temp -= 0.01
    
    def randomState(self):
        queenNum:int = -1
        destPos:int = -1

        isEqualToCurrent  = True
        while isEqualToCurrent:
            isEqualToCurrent = False

            queenNum = random.randint(0 , 7)
            destPos = random.randint(0 , 7)
            
            for pos in self.currentState.queensPosition:
                if queenNum == pos[0] and destPos == pos[1]:
                    isEqualToCurrent = True


        newState = self.currentState.moveQueen(queenNum , destPos)
        return newState
        
    def isNewStateValid(self , newState:State):
        if newState.evaluation < self.currentState.evaluation:
            return True
        
        deltaE = newState.evaluation - self.currentState.evaluation
        prop = math.exp(-1 * (deltaE / self.temp))
        print(prop)
        randomNum = random.random()

        if randomNum < prop:
            return True

        return False
