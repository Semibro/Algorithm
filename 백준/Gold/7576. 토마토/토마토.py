import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
queue = deque()
M, N = map(int, input().split())
tomato = [[-1] * (M+2) for _ in range(N+2)]

for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, M+1):
        tomato[i][j] = row[j-1]

for i in range(1, N+1):
    for j in range(1, M+1):
        if tomato[i][j] == 1:
            queue.append((i, j))

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while queue:
    t = queue.popleft()
    for d in delta:
        si, sj = t[0]+d[0], t[1]+d[1]
        if 1<=si<=N and 1<=sj<=M:
            if tomato[si][sj] == 0:
                tomato[si][sj] = tomato[t[0]][t[1]] + 1
                w = (si, sj)
                queue.append(w)

max_day = -1
for i in range(1, N+1):
    for j in range(1, M+1):
        if tomato[i][j] == 0:
            print(str(-1))
            exit()
    max_day = max(max_day, max(tomato[i]))

print(str(max_day-1))