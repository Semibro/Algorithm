from collections import deque
queue = deque()

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = []

for i in range(1, N+1):
    visited = [-1] * (N+1)
    visited[i] = 0
    v = i
    queue.append(v)
    while queue:
        t = queue.popleft()
        for j in graph[t]:
            if visited[j] == -1:
                queue.append(j)
                visited[j] = visited[t] + 1
    res = 0
    for k in visited:
        if k > 0:
            res += k
    result.append([res, i])
result.sort(key=lambda x:x[0])
print(result[0][1])