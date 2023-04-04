def solution(board):
    answer = 1
    N = len(board)
    o_cnt, x_cnt = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'O':
                o_cnt += 1
            elif board[i][j] == 'X':
                x_cnt += 1
    if o_cnt < x_cnt:
        answer = 0
    elif o_cnt == x_cnt:
        if o_cnt == 0 and x_cnt == 0:
            pass
        else:
            for i in board:
                if i == "OOO":
                    answer = 0
            if board[0][0] == board[1][1] == board[2][2] == 'O':
                answer = 0
            if board[2][0] == board[1][1] == board[0][2] == 'O':
                answer = 0
            if board[0][0] == board[1][0] == board[2][0] == 'O':
                answer = 0
            if board[0][1] == board[1][1] == board[2][1] == 'O':
                answer = 0
            if board[0][2] == board[1][2] == board[2][2] == 'O':
                answer = 0
    else:
        if o_cnt > x_cnt+1:
            answer = 0
        else:
            for i in board:
                if i == "XXX":
                    answer = 0
            if board[0][0] == board[1][1] == board[2][2] == 'X':
                answer = 0
            if board[2][0] == board[1][1] == board[0][2] == 'X':
                answer = 0
            if board[0][0] == board[1][0] == board[2][0] == 'X':
                answer = 0
            if board[0][1] == board[1][1] == board[2][1] == 'X':
                answer = 0
            if board[0][2] == board[1][2] == board[2][2] == 'X':
                answer = 0
    return answer