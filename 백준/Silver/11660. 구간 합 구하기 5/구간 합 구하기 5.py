import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    x = list(map(int, input().split()))
    for i in range(N-1):
        x[i+1] += x[i]
    board.append(x)
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    if y1 != 1:
        for j in range(x1-1, x2):
            answer += board[j][y2-1] - board[j][y1-2]
        print(answer)
    else:
        for j in range(x1-1, x2):
            answer += board[j][y2-1]
        print(answer)