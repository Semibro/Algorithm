from collections import deque

N, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(N)]
result = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
queue = deque()

for i in range(N):
    for j in range(M):
        if shark[i][j] == 1:
            queue.append((i, j))

while queue:
    t = queue.popleft()
    for d in delta:
        si, sj = t[0]+d[0], t[1]+d[1]
        if 0<=si<N and 0<=sj<M:
            if shark[si][sj] == 0:
                queue.append((si, sj))
                shark[si][sj] = shark[t[0]][t[1]] + 1

for i in range(N):
    for j in range(M):
        result = max(result, shark[i][j])

print(result - 1)