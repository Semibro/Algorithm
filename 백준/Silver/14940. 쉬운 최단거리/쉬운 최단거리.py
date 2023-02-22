from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start = (i, j)
            break

v = start
queue.append(v)
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while queue:
    t = queue.popleft()
    for d in delta:
        w = [t[0] + d[0], t[1] + d[1]]
        if 0 <= w[0] < n and 0 <= w[1] < m:
            if visited[w[0]][w[1]] == 0 and board[w[0]][w[1]] == 1:
                queue.append(w)
                visited[w[0]][w[1]] = visited[t[0]][t[1]] + 1

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] == 1:
            visited[i][j] = -1

for i in range(n):
    print(*visited[i])