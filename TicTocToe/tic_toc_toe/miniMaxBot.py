from tic_toc_toe.state import State


class MiniMaxBot:

    def __init__(self):
        pass
    def miniMax(self , state:State):
         newState = self.maxValue(state , -1000 , 1000)

         return newState

    def maxValue(self , state:State , alpha:int , beta:int):
        if state.isFinalState: return state

        returnState:State = None
        v = -1000
        preV = -1000
        for i in range(9):
            successor = state.changeBoard(i , 1)
            if successor == None:continue

            nextChildState:State = self.minValue(successor , alpha , beta)
            v = max(v , nextChildState.evaluation)
            if(preV != v):
                returnState = successor
                returnState.evaluation = nextChildState.evaluation
                preV = v

            if v > beta : 
                return returnState
            alpha = max(alpha , v)

        return returnState

    def minValue(self , state:State , alpha:int , beta:int):
        if state.isFinalState: return state

        returnState:State = None
        v = 1000
        preV = 1000
        for i in range(9):
            successor = state.changeBoard(i , -1)
            if successor == None: continue

            nextChildState:State = self.maxValue(successor , alpha , beta)
            
            v = min(v , nextChildState.evaluation)

            if(preV != v):
                returnState = successor
                returnState.evaluation = nextChildState.evaluation
                preV = v

            if v < alpha : 
                return returnState
            beta = min(beta , v)
                
        return returnState