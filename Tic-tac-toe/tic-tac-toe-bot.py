# Algorithm for Minimax:
# position : current position
# depth : how many more moves
# maximizingPlayer: boolean for is it the turn of maximising player
# def minimax(position,depth,maximizingPlayer):
#     if depth == 0 or game over in position:
#         return static evaluation of current position
#     if maximizingPlayer:
#         maxEval = -infinity
#         for each child of position:
#             eval = minimax(child,depth-1,false)
#             maxEval=max(maxEval,eval)
#         return maxEval
#     else:
#         minEval=+infinity
#         for each child of position:
#             eval = minimax(child,depth-1,true)
#             minEval=min(minEval,eval)
        
# create the board
board = [['_' for _ in range(3)]for _ in range(3)]
player = 'X'
ai = 'O'

#check if any moves are left (blank spaces)
def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

#find the winner : -1 for player, 1 for ai, 0 for draw : Ai is the maximising player
def winner(board):
    #checking rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0]!='_': #same value in full row 
            return 1 if row[0] ==ai else -1
    
    #checking columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]!='_':
            return 1 if board[0][col] == ai else -1
    
    #checking diagonals
    #left
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 1 if board[0][0] == ai else -1
    #right
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]!='_':
        return 1 if board[0][2] == ai else -1
    
    #draw
    return 0


def minimax(board,depth,maximising):
    score = winner(board)

    #if we have a winner
    if score == 1 or score ==-1:
        return score
    
    #if no moves left : draw
    if not is_moves_left(board):
        return 0
    
    #if no winner yet : return the best possible move in the current state
    if maximising:
        best = -10000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = ai
                    best = max(best, minimax(board, depth+1,False)) # why depth+1 : here we are using for how deep we are in the game (in above we are tracking how much is left, either works)
                    board[i][j]='_' #undo the move (backtrack)
        return best
    
    else:
        best = 10000
        for i in range(3):
            for j in range(3):
                if board[i][j]=='_':
                    board[i][j] = player
                    best = min(best, minimax(board,depth+1,True))
                    board[i][j]='_'
        return best
    
# find the best move for AI
def find_best_move(board):
    best_val = -10000
    best_move=(-1,-1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                #try move temporarily:
                board[i][j] = ai
                #evaluate the move
                move_val = minimax(board,0,False) # we are starting from 0 depth, also ai just played its human's turn so False
                board[i][j]='_'#undo move
                #if better result,store --> better means 0 better than -1 and 1 is best since that means AI wins
                if move_val>best_val:
                    best_move = (i,j)
                    best_val = move_val
    
    return best_move

def print_board(board):
    for row in board:
        print((' '.join(row)))
    print()

# --- Game loop ---
print("Tic-Tac-Toe Board (Positions):")
print("0 0 | 0 1 | 0 2")
print("1 0 | 1 1 | 1 2")
print("2 0 | 2 1 | 2 2")
print()

while True:
    print_board(board)

    # Check if game is over
    result = winner(board)
    if result == 1:
        print("AI wins!")
        break
    elif result == -1:
        print("You win!")
        break
    elif not is_moves_left(board):
        print("It's a draw!")
        break

    # Player move
    while True:
        try:
            x, y = map(int, input("Enter your move (row and col): ").split())
            if board[x][y] == '_':
                board[x][y] = player
                break
            else:
                print("Cell already taken. Try again.")
        except:
            print("Invalid input. Use format like: 0 1")

    # Check again after player's move
    result = winner(board)
    if result == -1:
        print_board(board)
        print("You win!")
        break
    elif not is_moves_left(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI move
    best_move = find_best_move(board)
    board[best_move[0]][best_move[1]] = ai

    





