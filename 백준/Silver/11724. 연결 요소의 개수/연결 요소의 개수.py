from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)
queue = deque()
cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        visited[i] = cnt
        queue.append(i)
        while queue:
            t = queue.popleft()
            for w in graph[t]:
                if visited[w] == 0:
                    visited[w] = cnt
                    queue.append(w)

print(max(visited))