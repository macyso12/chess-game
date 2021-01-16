from game import Game
from coord import Coord
from piece import Piece
from CLI import printGame,printValidMoves,printPossibleMoves
import testSets

def clearGame(g:Game):
    for c in [Coord(x,y) for x in range(8) for y in range(8)]:
        g.setSquare(c, Piece())

if __name__ == "__main__":
    g = Game()
    clearGame(g)

    g.setSquare(Coord(0,4), Piece("king", 0, 1, 0))
    g.setSquare(Coord(6,6), Piece("king", 1, 1, 0))
    printGame(g)
    for move in testSets.REPETITION_TEST:
        if(g.makeMove(move[0], move[1])):
            print("Able to make move")
        else:
            print("Unable to make move")
        printGame(g)
        
        print("Score:",g.getScore())
        print("Repetition stalemate:",g.checkRepetition())
    for move in g.log:
        print(f"Move {move[0]} -> {move[1]}")