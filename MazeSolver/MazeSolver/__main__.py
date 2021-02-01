from MazeSolver import aStar
from MazeSolver.mazeWorld import MazeWorld

if __name__ == "__main__":
    
    mazeWorld = MazeWorld(10, 10)
    root = mazeWorld.gnerateMaze()
    print("The maze gnerated")
    print("Algoritm started ....")
    path = aStar.aStarAlgoritm("1" , mazeWorld , "80")
    mazeWorld.drawTheMaze(root , "80" , "1")
    print("path : " +path)

