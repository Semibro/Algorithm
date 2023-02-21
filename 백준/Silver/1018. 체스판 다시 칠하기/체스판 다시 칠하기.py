def checker(board, i, j):
    cnt = 0
    cnt_2 = 0
    for k in range(8):
        for m in range(8):
            if (k+m) % 2 == 0:
                if board[i+k][j+m] == 'B':
                    cnt += 1
            else:
                if board[i+k][j+m] == 'W':
                    cnt += 1
    for k in range(8):
        for m in range(8):
            if (k + m) % 2 == 0:
                if board[i + k][j + m] == 'W':
                    cnt_2 += 1
            else:
                if board[i + k][j + m] == 'B':
                    cnt_2 += 1
    return min(cnt, cnt_2)

N, M = map(int, input().split()) # N:행, M:열
board = [list(input()) for _ in range(N)]
result_list = []
# 좌표
for i in range(0, N-7):
    for j in range(0, M-7):
        # 좌표를 기준으로 다른 곳 찾아서 count
        result_list.append(checker(board, i, j))

print(min(result_list))