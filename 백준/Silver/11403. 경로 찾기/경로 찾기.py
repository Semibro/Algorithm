from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
visited = [[0]*N for _ in range(N)]

for i in range(N):
    check = [0 for _ in range(N)]
    queue.append(i)
    while queue:
        x = queue.popleft()
        for j in range(N):
            if check[j] == 0 and graph[x][j] == 1:
                queue.append(j)
                check[j] = 1
                visited[i][j] = 1

for v in range(N):
    print(*visited[v])