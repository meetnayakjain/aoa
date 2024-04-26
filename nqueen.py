global N
N = 4

def solveNQ():
    board = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    if solveNQtill(board,0) == False:
        print('No solution')
        return False
    
    printSolution(board)
    return True

def solveNQtill(board,col):
    if col>=N:
        return True
    
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col]=1

            if solveNQtill(board,col+1)==True:
                return True
            board[i][col]=0
    return False

def isSafe(board,row,col):
    # row left
    for i in range(col):
        if board[row][i]==1:
            return False
        
    # upper left diagonal
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    
    # lower left diagonal
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
        
    return True

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                print('Q',end=" ")
            else:
                print(".",end=" ")
        print()

if __name__=="__main__":
    solveNQ()