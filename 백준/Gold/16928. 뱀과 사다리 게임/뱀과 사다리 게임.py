from collections import deque

N, M = map(int, input().split())
ladder, snake = {}, {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

bfs, visited = [0] * 101, [False] * 101
queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()
    for dice in range(1, 7):
        next_p = x + dice
        if next_p <= 100 and not visited[next_p]:
            if next_p in ladder.keys():
                next_p = ladder[next_p]
            if next_p in snake.keys():
                next_p = snake[next_p]
            if not visited[next_p]:
                visited[next_p] = True
                bfs[next_p] = bfs[x] + 1
                queue.append(next_p)

print(bfs[100])