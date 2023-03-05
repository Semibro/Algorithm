N = int(input())
board = [list(input()) for _ in range(N)]
max_v = 0

def check(board):
    global max_v
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
                if cnt > max_v:
                    max_v = cnt
            else:
                cnt = 1
        cnt = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                cnt += 1
                if cnt > max_v:
                    max_v = cnt
            else:
                cnt = 1

for i in range(N):
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        check(board)
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        check(board)
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(max_v)