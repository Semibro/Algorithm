board = [[0] * 1001 for _ in range(1001)]
N = int(input())
for i in range(1, N+1):
    a, b, w, h = map(int, input().split())
    for j in range(a, a+w):
        for k in range(b, b+h):
            board[j][k] = i

for i in range(1, N+1):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if board[j][k] == i:
                cnt += 1
    print(cnt)