from collections import deque

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
count, answer = 0, []

def bfs(x, y, temp):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    
    while queue:
        tx, ty = queue.popleft()
        for dx, dy in d:
            nx, ny = tx+dx, ty+dy
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                temp += 1
    
    return temp

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[M-i-1][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count += 1
            answer.append(bfs(i, j, 1))

answer.sort()
print(count)
for idx in range(len(answer)):
    print(answer[idx], end=" ")