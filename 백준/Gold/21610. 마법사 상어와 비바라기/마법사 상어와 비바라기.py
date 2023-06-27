import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
default = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    d, s = map(int, input().split())
    cloud = []

    # [1] 구름이동
    for cx, cy in default:
        dx, dy = (cx+delta[d][0]*s+N)%N, (cy+delta[d][1]*s+N)%N
        cloud.append((dx, dy))
        # [2] 물의 양 증가
        board[dx][dy] += 1
        # [3] 모든 구름이 사라진다

    # [4] 물복사버그
    visited = [[0]*N for _ in range(N)]
    for tx, ty in cloud:
        visited[tx][ty] = 1
        for ax, ay in ((1, 1), (-1, -1), (1, -1), (-1, 1)):
            sx, sy = tx+ax, ty+ay
            if 0<=sx<N and 0<=sy<N and board[sx][sy] > 0:
                board[tx][ty] += 1

    # [5] 구름이 있던 곳을 제외하고, 물의 양이 2이상인 칸에 모두 -2
    default = []
    for x in range(N):
        for y in range(N):
            # if board[x][y] >= 2 and (x, y) not in cloud:
            if board[x][y] >= 2 and not visited[x][y]:
                board[x][y] -= 2
                default.append((x, y))

answer = 0
for i in range(N):
    for j in range(N):
        answer += board[i][j]

print(answer)