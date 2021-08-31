def check_win(board):
    """
    Check if somebody win.
    Return winning symbol or None in case of tie
    """
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
        
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]

    if board[0][0] == board [1][1] == board [2][2]:
        return board[0][0]
    
    if board[0][2] == board [1][1] == board [2][0]:
        return board[0][2]

board = []
for r in range(3):
    line = input()
    board.append(line.split())

res = check_win(board)

if res.upper() == 'X':
    print('Anjali Wins')
elif res.upper() == 'O':
    print('Abhinav Wins')
else:
    print("Tie")