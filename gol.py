#life.py
#a program that simulates the game of life for a given number of iterations
#
#Alejandro Belgrave

import picture
ROUNDS = 500
WIDTH = 50
HEIGHT = 80

def boardSetup(board): #preset board configuration options.
    boardChoice = eval(input("Choose a configuration: "))
    if boardChoice == 1:
        board[0][2]=1
        board[0][3]=1
        board[1][2]=1
        board[10][0]=1
        board[17][3]= 1
        board[28][21]=1
        board[28][22] = 1
        board[28][23]=1
        board[2][3]=1
        board[3][1]=1
        board[35][38] = 1
        board[34][39]=1
        board[35][39]=1
        board[36][39]=1
        board[34][40]=1
        
    if boardChoice == 2:
        board[0][0]=1
        board[4][4]=1
        board[0][1]=1
        board[25][40]=1
        board[25][42]=1
        board[26][41]=1
        board[26][43]=1
        board[24][41]=1
        board[1][2]=1
        board[2][2]=1
        board[3][2]= 1
        board[16][38] = 1
        board[15][39]=1
        board[16][39]=1
        board[36][39]=1
        board[15][40]=1
        board[35][38] = 1
        board[34][39]=1
        board[35][39]=1
        board[36][39]=1
        board[34][40]=1
    
    if boardChoice==3:
        for i in range(0,40,25):
            for j in range(0,70,20):
                board[i+5][j+5]=1
                board[i+5][j+6]=1
                board[i+4][j+6]=1
                board[i+6][j+6]=1
                board[i+4][j+7]=1
        board[25][40]=1
        board[25][42]=1
        board[26][41]=1
        board[26][43]=1
        board[24][41]=1
    return board

def liveCount(board,newBoard):    #the method surverys neighboring cells and checks which cells are alive
    for row in range(WIDTH):
        for col in range(HEIGHT):
            living = 0
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    
                    if i%(WIDTH)==row and j%(HEIGHT)==col:
                        living = living + 0
                    elif board[i%(50)][j%(80)] == 1:
                            living = living +1
            if (living>=4) or (living<=1):
                newBoard[row][col] = 0
            elif (living == 3):
                newBoard[row][col] = 1
            else:
                newBoard[row][col] = board[row][col]
    return newBoard

def main():
# setting up the board
    board = []
    newBoard = []
    for i in range(WIDTH):
        board.append([0]*HEIGHT)
        newBoard.append([0]*HEIGHT)
    board = boardSetup(board)
    pic = picture.Picture((300,480))
    tiles = []
    pic.setOutlineColor((0,255,0))
    pic.setFillColor((0,0,0))
    for i in range(WIDTH):
        tiles.append([0]*HEIGHT) 
    for x in range(WIDTH):
        for y in range(HEIGHT):
            tiles[x][y] = pic.drawRectFill(x*6,y*6,6,6)
# traverses the board and checks if cell is alive, if the cell is alive, then it gets changed to red.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 1:
                tiles[x][y].changeFillColor((255,0,0))
# Iterates through each round and displays the progress as it occurs
    for i in range (ROUNDS-1):
        pic.display()
        newBoard = liveCount(board,newBoard)
        for l in range(WIDTH): # sets newBoard to board then changes color of cells of board
            for p in range(HEIGHT):
                board[l][p] = newBoard[l][p]
                if board[l][p] == 1:
                    tiles[l][p].changeFillColor((255,0,0))
                if board[l][p] == 0:
                    tiles[l][p].changeFillColor((0,0,0))
    pic.display()
    input()
 

main()