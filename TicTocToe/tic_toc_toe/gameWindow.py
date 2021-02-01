from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tic_toc_toe.miniMaxBot import MiniMaxBot
import time
import sys
from tic_toc_toe.state import State

class GameWindow(QMainWindow):
    app = QApplication(sys.argv)
    gameState:State
    bot = MiniMaxBot()
    isUserRole = True
    buttons:list[list[QPushButton]]

    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Python ") 
        self.setGeometry(100, 100, 300, 450)
        self.buttons = [] 
        self.UiComponents()
        self.show()
        self.gameState = self.firstState()
           
    def firstState(self):
        firstBoard = [[0,0,0],[0,0,0],[0,0,0]]
        firstState = State(firstBoard)
        return firstState

    def startGame(self):
        self.gameState = self.firstState()

        while not self.gameState.isFinalState:

            if(self.isUserRole):
                self.label.setText("Your Roll")

            while (self.isUserRole):
                QCoreApplication.processEvents()

            if not self.gameState.isFinalState:
                self.botAct()
            
            
        if(self.gameState.evaluation == 1): self.label.setText("the game over. you lose")
        elif (self.gameState.evaluation == 0): self.label.setText("the game over. draw")
        else : self.label.setText("the game over. you won")

        self.app.exec()
        # sys.exit() 

    # Computer and User Act method
    def userAct(self , state:State):
        button = self.sender()
        button.setEnabled(False) 
        buttonI = 0
        buttonJ = 0

        for i in range(3):
            for j in range(3):
                if( button == self.buttons[i][j]):
                     buttonI = i
                     buttonJ = j
        cellName = buttonI * 3 + buttonJ
        newState = self.gameState.changeBoard(int(cellName) , -1)
        self.gameState = newState
        button.setText("X") 
        self.isUserRole = False

    def botAct(self):
        newState = self.bot.miniMax(self.gameState)

        (i , j) = self.changedCellPossition(self.gameState , newState)

        button = self.buttons[i][j]
        self.gameState = newState
        button.setText("O") 
        button.setEnabled(False) 
        self.isUserRole = True

    def changedCellPossition(self , currentState:State , newState:State):
        for i in range(3):
            for j in range(3):
                if( currentState.board[i][j] != newState.board[i][j]):
                    return (i , j)

    # reset game method
    def resetGame(self):
        for btnList in self.buttons:
            for btn in btnList:
                btn.setEnabled(True)
                btn.setText("") 

        self.label.setText("your Roll")
        self.isUserRole = True

        self.startGame()
            
    # UI Gnerator
    def UiComponents(self):
        self.buttons = [] 
  
        for x in range(3): 
            temp = [] 
            for y in range(3): 
                temp.append((QPushButton(self))) 
            self.buttons.append(temp) 

        for i in range(3): 
            for j in range(3): 
                self.buttons[i][j].setGeometry(90*i + 20, 90*j + 20, 80, 80) 
                self.buttons[i][j].setFont(QFont(QFont('Times', 19))) 
                self.buttons[i][j].clicked.connect(self.userAct)
  
        self.label = QLabel(self) 
        self.label.setGeometry(20, 320, 260, 40) 
        self.label.setStyleSheet("QLabel{border : 1px solid blue; background : white;}") 
        self.label.setAlignment(Qt.AlignCenter) 
        self.label.setFont(QFont('Times', 15)) 
        reset_game = QPushButton("Restart", self) 
        reset_game.setGeometry(50, 380, 200, 30) 
        reset_game.clicked.connect(self.resetGame)